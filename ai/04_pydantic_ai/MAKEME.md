# Pydantic AI - Oefeningen

Maak deze oefeningen om hands-on ervaring op te doen met Pydantic AI. Start met de basis oefeningen en werk toe naar meer geavanceerde concepten.

## Setup
Zorg ervoor dat je de benodigde packages hebt geïnstalleerd:
```bash
pip install pydantic-ai[openai]
export OPENAI_API_KEY="your-api-key-here"
```

---

## 🟢 Basis Oefeningen

### Oefening 1: Eerste Agent
**Doel:** Maak je eerste Pydantic AI agent

**Opdracht:**
Schrijf een Python script dat:
1. Een eenvoudige Agent aanmaakt
2. Een vraag stelt over je favoriete programmeertaal
3. Het antwoord afdrukt

**Startcode:**
```python
from pydantic_ai import Agent

# Jouw code hier
agent = Agent(...)
result = agent.run_sync("...")
print(result.data)
```

### Oefening 2: Boek Informatie
**Doel:** Gebruik gestructureerde outputs voor boekinformatie

**Opdracht:**
1. Maak een `BoekInfo` Pydantic model met:
   - titel (str)
   - auteur (str)
   - genre (str)
   - publicatiejaar (int)
   - paginas (int)
   - samenvatting (str)

2. Maak een agent die informatie over een boek ophaalt
3. Test met "Harry Potter en de Steen der Wijzen"

**Verwacht resultaat:**
```python
boek = result.data
print(f"{boek.titel} door {boek.auteur}")
print(f"Genre: {boek.genre} ({boek.publicatiejaar})")
```

### Oefening 3: Weer Voorspelling
**Doel:** Werk met validatie en constraints

**Opdracht:**
1. Maak een `WeerVoorspelling` model met:
   - locatie (str)
   - temperatuur (int, tussen -50 en 60)
   - luchtvochtigheid (int, tussen 0 en 100)
   - beschrijving (str)
   - regenkanss (float, tussen 0.0 en 1.0)

2. Vraag om weersvoorspelling voor verschillende steden
3. Test de validatie door edge cases te proberen

---

## 🟡 Tussenliggende Oefeningen

### Oefening 4: Product Review Analyzer
**Doel:** Sentiment analyse met gestructureerde output

**Opdracht:**
1. Maak een `ProductReview` model met:
   - product_naam (str)
   - overall_rating (int, 1-5)
   - positieve_punten (List[str])
   - negatieve_punten (List[str])
   - aanbeveling (bool)
   - doelgroep (str)

2. Maak een agent die productreviews analyseert
3. Test met verschillende review teksten

**Test data:**
```python
review_tekst = """
Deze laptop is fantastisch voor programmeren! De batterij gaat 8 uur mee, 
het scherm is helder en het toetsenbord voelt geweldig aan. Alleen is hij 
wat zwaar voor dagelijks reizen. Perfect voor studenten informatica.
"""
```

### Oefening 5: Recept Generator met System Prompt
**Doel:** System prompts en context gebruiken

**Opdracht:**
1. Maak een `Recept` model (zie TRYME.py voor inspiratie)
2. Schrijf een system prompt die:
   - Alleen vegetarische recepten geeft
   - Ingrediënten beperkt tot max 8 items
   - Bereidingstijd onder 30 minuten houdt
3. Test met verschillende gerechten

### Oefening 6: Code Reviewer
**Doel:** Gestructureerde code analyse

**Opdracht:**
1. Maak een `CodeReview` model met:
   - taal (str)
   - kwaliteit_score (int, 1-10)
   - verbeterpunten (List[str])
   - goede_punten (List[str])
   - beveiligingsrisicos (List[str])
   - refactor_suggesties (List[str])

2. Maak een agent die Python code analyseert
3. Test met verschillende code snippets

**Test code:**
```python
code_snippet = '''
def calculate_total(items):
    total = 0
    for item in items:
        total = total + item['price'] * item['quantity']
    return total

items = [{'price': 10, 'quantity': 2}, {'price': 5, 'quantity': 3}]
print(calculate_total(items))
'''
```

---

## 🔴 Geavanceerde Oefeningen

### Oefening 7: Multi-format Response
**Doel:** Union types en flexible outputs

**Opdracht:**
1. Maak models voor verschillende response types:
   - `SuccessResponse` (success: bool, data: dict)
   - `ErrorResponse` (success: bool, error_message: str, error_code: int)

2. Gebruik Union[SuccessResponse, ErrorResponse] als result_type
3. Maak een agent die soms succesvol is, soms faalt

### Oefening 8: Conversation Memory
**Doel:** Multi-turn conversations met context

**Opdracht:**
1. Maak een `ConversationTurn` model voor gesprekken
2. Implementeer een chatbot die:
   - Eerdere berichten onthoudt
   - Context gebruikt voor vervolgvragen
   - Consistente persoonlijkheid heeft

3. Test een multi-turn conversatie

### Oefening 9: Tool Integration
**Doel:** Agents met externe tools

**Opdracht:**
1. Maak functies voor:
   - `zoek_wikipedia(term: str) -> dict`
   - `bereken_wiskundige_expressie(expressie: str) -> float`

2. Integreer deze als tools in een agent
3. Test complexe vragen die meerdere tools vereisen

**Voorbeeld vraag:** "Wat is de oppervlakte van Nederland gedeeld door het aantal inwoners?"

### Oefening 10: Custom Validation
**Doel:** Geavanceerde Pydantic features

**Opdracht:**
1. Maak een `EmailCampagne` model met:
   - Custom validators voor email formaten
   - Conditional validation (als type == "newsletter", dan required fields)
   - Custom serializers

2. Implementeer error handling voor validation failures
3. Test edge cases en error scenarios

---

## 🏆 Bonus Projecten

### Project A: AI-Powered Recipe Assistant
Bouw een complete recipe assistant die:
- Recepten genereert op basis van beschikbare ingrediënten
- Dieetbeperkingen respecteert (vegetarisch, glutenvrij, etc.)
- Kooktips geeft
- Ingrediëntenlijst optimaliseert

### Project B: Code Quality Dashboard
Maak een tool die:
- Meerdere code bestanden analyseert
- Quality metrics berekent
- Refactoring roadmap genereert
- Progress tracking implementeert

### Project C: Smart Content Moderator
Ontwikkel een content moderatie tool die:
- Tekst classificeert (spam, toxic, normal)
- Confidence scores geeft
- Explanation genereert voor beslissingen
- False positive detection implementeert

---

## 📋 Antwoorden Checklist

Voor elke oefening, controleer:
- [ ] Pydantic model is correct gedefinieerd
- [ ] Agent wordt juist geïnitialiseerd
- [ ] Error handling is geïmplementeerd
- [ ] Output is leesbaar en informatief
- [ ] Code volgt Python best practices
- [ ] Validatie werkt zoals verwacht

## 💡 Tips voor Success

1. **Start klein:** Begin met eenvoudige models en bouw langzaam uit
2. **Test validatie:** Probeer bewust ongeldige inputs
3. **Gebruik type hints:** Maak je code self-documenting
4. **Experimenteer met prompts:** Kleine wijzigingen kunnen grote impact hebben
5. **Lees error messages:** Pydantic geeft zeer informatieve foutmeldingen
6. **Bekijk de logs:** Gebruik debugging om AI-interacties te begrijpen

## 🔍 Troubleshooting

**API Key problemen:**
```bash
echo $OPENAI_API_KEY  # Controleer of key is ingesteld
```

**Import errors:**
```bash
pip list | grep pydantic  # Controleer installatie
pip install --upgrade pydantic-ai
```

**Validation errors:**
- Controleer field types in je Pydantic models
- Gebruik Field() voor constraints en descriptions
- Test met eenvoudige inputs eerst

**AI Response kwaliteit:**
- Maak system prompts specifieker
- Gebruik voorbeelden in je prompts
- Experimenteer met verschillende models (gpt-3.5 vs gpt-4)

---

Veel succes met de oefeningen! 🚀