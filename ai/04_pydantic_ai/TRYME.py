#!/usr/bin/env python3
"""
Pydantic AI - Praktische voorbeelden
====================================

Dit bestand bevat werkende voorbeelden van Pydantic AI.
Voer de scripts uit om te zien hoe gestructureerde AI-outputs werken.

Requirements:
pip install pydantic-ai[openai]

Setup:
export OPENAI_API_KEY="your-api-key-here"
"""

import os
from typing import List, Optional
from pydantic import BaseModel, Field
from pydantic_ai import Agent

# Controleer of API key is ingesteld
if not os.getenv('OPENAI_API_KEY'):
    print("⚠️  OPENAI_API_KEY environment variable niet ingesteld!")
    print("Gebruik: export OPENAI_API_KEY='your-api-key-here'")
    exit(1)


# =============================================================================
# Voorbeeld 1: Eenvoudige string response
# =============================================================================

def voorbeeld1_eenvoudige_response():
    """Basis voorbeeld met string output"""
    print("🔹 Voorbeeld 1: Eenvoudige string response")
    print("-" * 50)
    
    agent = Agent('openai:gpt-3.5-turbo')
    
    try:
        result = agent.run_sync('Wat is de hoofdstad van Frankrijk?')
        print(f"Vraag: Wat is de hoofdstad van Frankrijk?")
        print(f"Antwoord: {result.data}")
    except Exception as e:
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


def voorbeeld2_gestructureerde_output():
    """Gestructureerde output met Pydantic model"""
    print("🔹 Voorbeeld 2: Gestructureerde output")
    print("-" * 50)
    
    agent = Agent('openai:gpt-3.5-turbo', result_type=PersonInfo)
    
    try:
        result = agent.run_sync('Geef informatie over Albert Einstein')
        person = result.data
        
        print(f"Naam: {person.naam}")
        print(f"Leeftijd: {person.leeftijd}")
        print(f"Beroep: {person.beroep}")
        print(f"Nationaliteit: {person.nationaliteit}")
        print(f"Bekend voor: {', '.join(person.bekend_voor)}")
    except Exception as e:
        print(f"Fout: {e}")
    
    print()


# =============================================================================
# Voorbeeld 3: System prompt en context
# =============================================================================

class Recept(BaseModel):
    """Model voor een recept"""
    naam: str = Field(description="Naam van het gerecht")
    porties: int = Field(description="Aantal porties", ge=1)
    bereidingstijd: int = Field(description="Bereidingstijd in minuten")
    ingredienten: List[str] = Field(description="Lijst van ingrediënten met hoeveelheden")
    instructies: List[str] = Field(description="Stap-voor-stap instructies")
    moeilijkheidsgraad: str = Field(description="Makkelijk, Gemiddeld, of Moeilijk")


def voorbeeld3_system_prompt():
    """Agent met system prompt voor consistente output"""
    print("🔹 Voorbeeld 3: System prompt en context")
    print("-" * 50)
    
    agent = Agent(
        'openai:gpt-3.5-turbo',
        result_type=Recept,
        system_prompt="""
        Je bent een ervaren chef-kok die eenvoudige, haalbare recepten geeft.
        Gebruik alleen ingrediënten die makkelijk te vinden zijn in een Nederlandse supermarkt.
        Geef duidelijke, stapsgewijze instructies.
        Houd bereidingstijden realistisch.
        """
    )
    
    try:
        result = agent.run_sync('Maak een recept voor spaghetti carbonara voor 2 personen')
        recept = result.data
        
        print(f"📝 Recept: {recept.naam}")
        print(f"👥 Porties: {recept.porties}")
        print(f"⏱️  Bereidingstijd: {recept.bereidingstijd} minuten")
        print(f"📊 Moeilijkheidsgraad: {recept.moeilijkheidsgraad}")
        
        print(f"\n🛒 Ingrediënten:")
        for ingredient in recept.ingredienten:
            print(f"  • {ingredient}")
        
        print(f"\n👨‍🍳 Instructies:")
        for i, instructie in enumerate(recept.instructies, 1):
            print(f"  {i}. {instructie}")
            
    except Exception as e:
        print(f"Fout: {e}")
    
    print()


# =============================================================================
# Voorbeeld 4: Sentiment analyse
# =============================================================================

class SentimentAnalyse(BaseModel):
    """Model voor sentiment analyse"""
    tekst: str = Field(description="De originele tekst")
    sentiment: str = Field(description="Positief, Negatief, of Neutraal")
    score: float = Field(description="Sentiment score tussen -1 (zeer negatief) en 1 (zeer positief)")
    emoties: List[str] = Field(description="Lijst van gedetecteerde emoties")
    belangrijkste_themas: List[str] = Field(description="Hoofdthema's in de tekst")
    samenvatting: str = Field(description="Korte samenvatting van de sentiment analyse")


def voorbeeld4_sentiment_analyse():
    """Sentiment analyse van tekst"""
    print("🔹 Voorbeeld 4: Sentiment analyse")
    print("-" * 50)
    
    agent = Agent(
        'openai:gpt-3.5-turbo',
        result_type=SentimentAnalyse,
        system_prompt="""
        Je bent een expert in sentiment analyse en emotie detectie.
        Analyseer de gegeven tekst objectief en geef een uitgebreide analyse.
        Gebruik Nederlandse termen voor emoties en sentimenten.
        """
    )
    
    test_tekst = """
    Ik ben echt teleurgesteld in deze nieuwe smartphone. De camera kwaliteit is veel slechter 
    dan beloofd en de batterij gaat veel te snel leeg. Na twee dagen gebruik moet ik hem al 
    drie keer per dag opladen! De klantenservice was ook niet behulpzaam toen ik belde. 
    Ik had veel meer verwacht voor deze prijs.
    """
    
    try:
        result = agent.run_sync(f'Analyseer het sentiment van deze tekst: {test_tekst}')
        analyse = result.data
        
        print(f"📱 Originele tekst: {analyse.tekst[:100]}...")
        print(f"😊 Sentiment: {analyse.sentiment}")
        print(f"📊 Score: {analyse.score:.2f}")
        print(f"💭 Emoties: {', '.join(analyse.emoties)}")
        print(f"🎯 Thema's: {', '.join(analyse.belangrijkste_themas)}")
        print(f"📝 Samenvatting: {analyse.samenvatting}")
        
    except Exception as e:
        print(f"Fout: {e}")
    
    print()


# =============================================================================
# Voorbeeld 5: Multi-stap conversatie
# =============================================================================

class VerhaalElement(BaseModel):
    """Model voor een verhaal element"""
    karakter: str = Field(description="Hoofdkarakter in het verhaal")
    setting: str = Field(description="Waar en wanneer het verhaal plaatsvindt")
    conflict: str = Field(description="Het hoofdconflict of probleem")
    plot_punten: List[str] = Field(description="Belangrijke gebeurtenissen in chronologische volgorde")
    thema: str = Field(description="Het centrale thema van het verhaal")
    genre: str = Field(description="Het genre van het verhaal")


def voorbeeld5_verhaal_generator():
    """Multi-stap verhaal generatie"""
    print("🔹 Voorbeeld 5: Verhaal generator")
    print("-" * 50)
    
    agent = Agent(
        'openai:gpt-3.5-turbo',
        result_type=VerhaalElement,
        system_prompt="""
        Je bent een creatieve schrijver die boeiende korte verhalen bedenkt.
        Maak interessante karakters en onverwachte wendingen.
        Houd verhalen geschikt voor alle leeftijden.
        """
    )
    
    try:
        # Eerste prompt
        result = agent.run_sync("""
        Bedenk een kort verhaal over een robot die leert wat vriendschap betekent.
        Het verhaal moet plaatsvinden in een futuristische stad.
        """)
        
        verhaal = result.data
        
        print(f"🤖 Karakter: {verhaal.karakter}")
        print(f"🏙️  Setting: {verhaal.setting}")
        print(f"⚡ Conflict: {verhaal.conflict}")
        print(f"🎭 Genre: {verhaal.genre}")
        print(f"💡 Thema: {verhaal.thema}")
        
        print(f"\n📖 Plot punten:")
        for i, punt in enumerate(verhaal.plot_punten, 1):
            print(f"  {i}. {punt}")
            
    except Exception as e:
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
    voorbeeld1_eenvoudige_response()
    voorbeeld2_gestructureerde_output()
    voorbeeld3_system_prompt()
    voorbeeld4_sentiment_analyse()
    voorbeeld5_verhaal_generator()
    
    print("✅ Alle voorbeelden uitgevoerd!")
    print("\n💡 Tips:")
    print("  • Experimenteer met verschillende prompts")
    print("  • Probeer andere AI-modellen (gpt-4, claude, etc.)")
    print("  • Maak je eigen Pydantic models")
    print("  • Test error handling met ongeldige inputs")


if __name__ == "__main__":
    main()