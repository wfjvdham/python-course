#!/usr/bin/env python3
"""
Pydantic AI - Praktische voorbeelden
====================================

Dit bestand bevat werkende voorbeelden van Pydantic AI met Anthropic (Claude) modellen.
Voer de scripts uit om te zien hoe gestructureerde AI-outputs werken.

Setup:
    export ANTHROPIC_API_KEY="your-api-key-here"

Aanpassen model:
    Wijzig de MODEL constante beneden om een ander Claude model te testen.
"""

import os
from dataclasses import dataclass, field
from typing import List, Optional, Annotated
from pydantic import BaseModel, Field, conlist
from pydantic_ai import Agent, RunContext

MODEL = 'anthropic:claude-3-haiku-20240307'

# Controleer of Anthropic API key is ingesteld
if not os.getenv('ANTHROPIC_API_KEY'):
    print("⚠️  ANTHROPIC_API_KEY environment variable niet ingesteld!")
    print("Gebruik: export ANTHROPIC_API_KEY='your-api-key-here'")
    exit(1)


# =============================================================================
# Voorbeeld 1: Eenvoudige string response
# =============================================================================

def voorbeeld1_eenvoudige_response():
    """Basis voorbeeld met string output"""
    print("🔹 Voorbeeld 1: Eenvoudige string response")
    print("-" * 50)

    agent = Agent(MODEL)  # default output_type = str
    vraag = 'Wat is de hoofdstad van Frankrijk?'
    try:
        result = agent.run_sync(vraag)
        print(f"Vraag: {vraag}")
        print(f"Antwoord: {result}")
    except Exception as e:  # noqa: BLE001
        print(f"Fout: {e}")

    print()


# =============================================================================
# Voorbeeld 2: Gestructureerde output met Pydantic
# =============================================================================

class PersonInfo(BaseModel):
    """Model voor persooninformatie"""
    naam: str = Field(description="De volledige naam van de persoon")
    leeftijd: int = Field(description="Leeftijd in jaren", ge=0, le=150)
    beroep: str = Field(description="Het huidige beroep")
    nationaliteit: str = Field(description="De nationaliteit")
    bekend_voor: List[str] = Field(description="Lijst van dingen waar persoon bekend voor staat")


@dataclass
class PersonDeps:
    """Dependencies voor persoons-informatie"""
    taal: str = "nl"
    detailniveau: str = "compact"


person_agent = Agent(
    MODEL,
    deps_type=PersonDeps,
    output_type=PersonInfo,
    instructions="Je bent een expert in biografie en wetenschapsgeschiedenis. Geef accurate, beknopte informatie.",
)


@person_agent.instructions
def add_context_instructions(ctx: RunContext[PersonDeps]) -> str:
    return f"Antwoord in het {ctx.deps.taal} met {ctx.deps.detailniveau} detail niveau."


def voorbeeld2_gestructureerde_output():
    """Gestructureerde output met Pydantic model via decorators"""
    print("🔹 Voorbeeld 2: Gestructureerde output (decorator pattern)")
    print("-" * 50)

    prompt = "Beschrijf Albert Einstein in de gevraagde velden."
    try:
        result = person_agent.run_sync(prompt, deps=PersonDeps(taal="nl", detailniveau="beknopt"))
        person = result.output
        
        print(f"Naam: {person.naam}")
        print(f"Leeftijd: {person.leeftijd}")
        print(f"Beroep: {person.beroep}")
        print(f"Nationaliteit: {person.nationaliteit}")
        print(f"Bekend voor: {', '.join(person.bekend_voor)}")
    except Exception as e:  # noqa: BLE001
        print(f"Fout: {e}")

    print()


# =============================================================================
# Voorbeeld 3: Recept generator met tools
# =============================================================================

class Recept(BaseModel):
    """Model voor een recept"""
    naam: str = Field(description="Naam van het gerecht")
    porties: int = Field(description="Aantal porties", ge=1)
    bereidingstijd: int = Field(description="Bereidingstijd in minuten")
    ingredienten: List[str] = Field(description="Lijst van ingrediënten met hoeveelheden")
    instructies: List[str] = Field(description="Stap-voor-stap instructies")
    moeilijkheidsgraad: str = Field(description="Makkelijk, Gemiddeld, of Moeilijk")


@dataclass
class ChefDeps:
    """Dependencies voor chef agent"""
    doelgroep: str = "beginners"
    keuken_type: str = "nederlands"
    dieet_restricties: Optional[List[str]] = None


chef_agent = Agent(
    MODEL,
    deps_type=ChefDeps,
    output_type=Recept,
    instructions=(
        "Je bent een ervaren chef-kok die eenvoudige, haalbare recepten geeft. "
        "Gebruik ingrediënten die makkelijk te vinden zijn."
    ),
)


@chef_agent.instructions
def add_chef_context(ctx: RunContext[ChefDeps]) -> str:
    context = f"Pas het recept aan voor {ctx.deps.doelgroep} in de {ctx.deps.keuken_type} keuken."
    if ctx.deps.dieet_restricties:
        context += f" Houd rekening met dieet restricties: {', '.join(ctx.deps.dieet_restricties)}."
    return context


@chef_agent.tool
def get_seasonal_ingredients(ctx: RunContext[ChefDeps], month: int) -> List[str]:
    """Geeft seizoensgebonden ingrediënten voor een specifieke maand (1-12)."""
    seasonal_map = {
        1: ["winterpeen", "spruitjes", "rode kool"],
        2: ["winterpeen", "spruitjes", "rode kool"],
        3: ["asperges", "radijs", "spinazie"],
        4: ["asperges", "radijs", "spinazie", "aardbeien"],
        5: ["aardbeien", "asperges", "tuinbonen"],
        6: ["aardbeien", "courgette", "tuinbonen"],
        7: ["tomaten", "komkommer", "courgette"],
        8: ["tomaten", "komkommer", "paprika"],
        9: ["pompoen", "appels", "broccoli"],
        10: ["pompoen", "appels", "broccoli"],
        11: ["winterpeen", "spruitjes", "pastinaken"],
        12: ["winterpeen", "spruitjes", "rode kool"]
    }
    return seasonal_map.get(month, [])


def voorbeeld3_system_prompt():
    """Agent met system prompt + tools"""
    print("🔹 Voorbeeld 3: Recept generator (decorator pattern)")
    print("-" * 50)

    prompt = 'Maak een recept voor spaghetti carbonara voor 2 personen.'
    try:
        deps = ChefDeps(doelgroep="beginners", keuken_type="italiaans")
        result = chef_agent.run_sync(prompt, deps=deps)
        recept = result.output
        print(f"📝 Recept: {recept.naam}")
        print(f"👥 Porties: {recept.porties}")
        print(f"⏱️  Bereidingstijd: {recept.bereidingstijd} minuten") 
        print(f"📊 Moeilijkheidsgraad: {recept.moeilijkheidsgraad}")  
        print("\n🛒 Ingrediënten:")
        for ingredient in recept.ingredienten:  
            print(f"  • {ingredient}")
        print("\n👨‍🍳 Instructies:")
        for i, instructie in enumerate(recept.instructies, 1): 
            print(f"  {i}. {instructie}")
    except Exception as e:  # noqa: BLE001
        print(f"Fout: {e}")

    print()


# =============================================================================
# Voorbeeld 4: Sentiment analyse met context
# =============================================================================

class SentimentAnalyse(BaseModel):
    """Model voor sentiment analyse"""
    tekst: str = Field(description="De originele tekst (verkort tot max 100 karakters)", max_length=100)
    sentiment: str = Field(description="Sentiment: Positief, Negatief, of Neutraal")
    score: float = Field(description="Sentiment score tussen -1 (zeer negatief) en 1 (zeer positief)", ge=-1.0, le=1.0)
    emoties: conlist(str, min_length=1, max_length=5) = Field(description="Lijst van 1-5 gedetecteerde emoties")  # type: ignore
    belangrijkste_themas: conlist(str, min_length=1, max_length=3) = Field(description="1-3 hoofdthema's in de tekst")  # type: ignore
    samenvatting: str = Field(description="Korte samenvatting (max 200 karakters)", max_length=200)


@dataclass
class AnalyseDeps:
    """Dependencies voor sentiment analyse"""
    taal: str = "nl"
    toon: str = "objectief"
    focus_areas: Optional[List[str]] = None


sentiment_agent = Agent(
    MODEL,
    deps_type=AnalyseDeps,
    output_type=SentimentAnalyse,
    retries=3,  # Increase retries for validation
    instructions=(
        "Je bent een expert in sentiment analyse en emotie detectie. "
        "Analyseer teksten objectief en geef uitgebreide analyses. "
        "BELANGRIJK: "
        "- sentiment moet exact 'Positief', 'Negatief', of 'Neutraal' zijn "
        "- score moet tussen -1.0 en 1.0 liggen "
        "- emoties: geef 1-5 Nederlandse emotiewoorden "
        "- themas: geef 1-3 kernthema's "
        "- houd tekstvelden kort en duidelijk"
    ),
)


@sentiment_agent.instructions
def add_analysis_context(ctx: RunContext[AnalyseDeps]) -> str:
    context = f"Voer de analyse uit in het {ctx.deps.taal} met een {ctx.deps.toon} toon."
    if ctx.deps.focus_areas:
        context += f" Focus vooral op: {', '.join(ctx.deps.focus_areas)}."
    return context


@sentiment_agent.tool
def get_emotion_categories(ctx: RunContext[AnalyseDeps]) -> List[str]:
    """Geeft beschikbare emotie categorieën voor de analyse."""
    if ctx.deps.taal == "nl":
        return [
            "vreugde", "verdriet", "woede", "angst", "verrassing", 
            "walging", "teleurstelling", "frustratie", "enthousiasme", "tevredenheid"
        ]
    return [
        "joy", "sadness", "anger", "fear", "surprise", 
        "disgust", "disappointment", "frustration", "enthusiasm", "satisfaction"
    ]


def voorbeeld4_sentiment_analyse():
    """Sentiment analyse met tools en context"""
    print("🔹 Voorbeeld 4: Sentiment analyse (decorator pattern)")
    print("-" * 50)

    test_tekst = (
        "Ik ben echt teleurgesteld in deze nieuwe smartphone. De camera kwaliteit is veel slechter dan beloofd en de batterij "
        "gaat veel te snel leeg. Na twee dagen gebruik moet ik hem al drie keer per dag opladen! De klantenservice was ook "
        "niet behulpzaam. Ik had veel meer verwacht voor deze prijs."
    )

    prompt = f"Voer een sentiment analyse uit over deze tekst: '''{test_tekst}'''"
    try:
        deps = AnalyseDeps(taal="nl", toon="objectief", focus_areas=["product_ervaring", "klantenservice"])
        result = sentiment_agent.run_sync(prompt, deps=deps)
        analyse = result.output
        print(f"📱 Originele tekst: {analyse.tekst[:100]}...")
        print(f"😊 Sentiment: {analyse.sentiment}")
        print(f"📊 Score: {analyse.score:.2f}")
        print(f"💭 Emoties: {', '.join(analyse.emoties)}")
        print(f"🎯 Thema's: {', '.join(analyse.belangrijkste_themas)}")
        print(f"📝 Samenvatting: {analyse.samenvatting}")
    except Exception as e:  # noqa: BLE001
        print(f"Fout: {e}")
        print(f"Type: {type(e)}")

    print()


# =============================================================================
# Voorbeeld 5: Verhaal generator met tools
# =============================================================================

class VerhaalElement(BaseModel):
    """Model voor een verhaal element"""
    karakter: str = Field(description="Hoofdkarakter in het verhaal")
    setting: str = Field(description="Waar en wanneer het verhaal plaatsvindt")
    conflict: str = Field(description="Het hoofdconflict of probleem")
    plot_punten: List[str] = Field(description="Belangrijke gebeurtenissen in chronologische volgorde")
    thema: str = Field(description="Het centrale thema van het verhaal")
    genre: str = Field(description="Het genre van het verhaal")


@dataclass
class StoryDeps:
    """Dependencies voor verhaal generator"""
    doelgroep: str = "algemeen"
    leeftijdscategorie: str = "alle_leeftijden"
    verhaal_lengte: str = "kort"


story_agent = Agent(
    MODEL,
    deps_type=StoryDeps,
    output_type=VerhaalElement,
    instructions=(
        "Je bent een creatieve schrijver die boeiende verhalen bedenkt met interessante karakters en onverwachte wendingen."
    ),
)


@story_agent.instructions
def add_story_context(ctx: RunContext[StoryDeps]) -> str:
    return (
        f"Maak een {ctx.deps.verhaal_lengte} verhaal geschikt voor {ctx.deps.doelgroep} "
        f"({ctx.deps.leeftijdscategorie}). Houd het passend voor de doelgroep."
    )


@story_agent.tool
def get_genre_elements(ctx: RunContext[StoryDeps], genre: str) -> List[str]:
    """Geeft typische elementen voor een specifiek genre."""
    genre_elements = {
        "science_fiction": ["technologie", "ruimte", "robots", "toekomst", "aliens"],
        "fantasy": ["magie", "draken", "tovenaars", "queeste", "mythische_wezens"],
        "thriller": ["spanning", "mysterie", "achtervolging", "gevaar", "plot_twist"],
        "romance": ["liefde", "relaties", "emoties", "ontmoeting", "conflict"],
        "humor": ["grappige_situaties", "woordspelingen", "onverwachte_wendingen", "karakterfouten"]
    }
    return genre_elements.get(genre.lower(), ["verhaal_elementen"])


def voorbeeld5_verhaal_generator():
    """Verhaal generator met tools"""
    print("🔹 Voorbeeld 5: Verhaal generator (decorator pattern)")
    print("-" * 50)

    prompt = (
        "Genereer de verhaalstructuur voor een kort verhaal over een robot die leert wat vriendschap betekent in een futuristische stad."
    )
    try:
        deps = StoryDeps(doelgroep="jongeren", leeftijdscategorie="12+", verhaal_lengte="kort")
        result = story_agent.run_sync(prompt, deps=deps)
        verhaal = result.output
        print(f"🤖 Karakter: {verhaal.karakter}")
        print(f"🏙️  Setting: {verhaal.setting}")
        print(f"⚡ Conflict: {verhaal.conflict}")
        print(f"🎭 Genre: {verhaal.genre}")
        print(f"💡 Thema: {verhaal.thema}")
        print("\n📖 Plot punten:")
        for i, punt in enumerate(verhaal.plot_punten, 1):  # type: ignore
            print(f"  {i}. {punt}")
    except Exception as e:  # noqa: BLE001
        print(f"Fout: {e}")

    print()


# =============================================================================
# Main functie - voer alle voorbeelden uit
# =============================================================================

def main():
    """Voer alle voorbeelden uit"""
    print("🚀 Pydantic AI Voorbeelden")
    print("=" * 70)
    print()
    
    # Voer voorbeelden uit
    # voorbeeld1_eenvoudige_response()
    # voorbeeld2_gestructureerde_output()
    # voorbeeld3_system_prompt()
    # voorbeeld4_sentiment_analyse()
    # voorbeeld5_verhaal_generator()
    
    print("✅ Alle voorbeelden uitgevoerd!")
    print("\n💡 Tips:")
    print("  • Experimenteer met verschillende prompts")
    print("  • Probeer andere AI-modellen (gpt-4, claude, etc.)")
    print("  • Maak je eigen Pydantic models")
    print("  • Test error handling met ongeldige inputs")


if __name__ == "__main__":
    main()