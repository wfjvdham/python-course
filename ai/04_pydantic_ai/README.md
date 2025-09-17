# Pydantic AI

Dit hoofdstuk legt uit hoe je Pydantic AI gebruikt voor type-safe AI-applicaties met gestructureerde outputs. Pydantic AI combineert de kracht van Pydantic's datavalidatie met AI-modellen voor betrouwbare en voorspelbare resultaten.

## Inhoud
1. Wat is Pydantic AI?
2. Installatie en setup
3. Basis concepten
4. Praktische voorbeelden
5. Oefeningen

---

## 1. Wat is Pydantic AI?

Pydantic AI is een Python-framework dat de betrouwbaarheid van AI-applicaties verbetert door:
- **Type safety**: Gebruik Pydantic models voor gestructureerde AI-outputs
- **Validatie**: Automatische validatie van AI-responses
- **Integration**: Eenvoudige integratie met populaire AI-providers
- **Debugging**: Betere foutafhandeling en debugging van AI-interacties

### Waarom Pydantic AI?

| Probleem zonder Pydantic AI | Oplossing met Pydantic AI |
|----------------------------|---------------------------|
| Onvoorspelbare AI-output formats | Gedefinieerde Pydantic schemas |
| Moeilijk te debuggen AI-responses | Type hints en validatie |
| Inconsistente data parsing | Automatische deserialisatie |
| Runtime errors door malformed data | Compile-time type checking |

## 2. Installatie en setup

```bash
uv add pydantic-ai
# Voor OpenAI support
uv add pydantic-ai[openai]
# Voor Anthropic support  
uv add pydantic-ai[anthropic]
```

### Environment setup
```bash
# Voor OpenAI
export OPENAI_API_KEY="your-api-key-here"
# Voor Anthropic
export ANTHROPIC_API_KEY="your-api-key-here"
```

## 3. Basis concepten

### Agent
Een `Agent` is het centrale concept in Pydantic AI - het definieert:
- Het AI-model dat gebruikt wordt
- Het response format (Pydantic model)
- System prompts en gedrag

### Result Types
Pydantic AI ondersteunt verschillende result types:
- **str**: Eenvoudige string responses
- **Pydantic Models**: Gestructureerde data
- **Union Types**: Meerdere mogelijke response formats

### Structured Outputs
Het belangrijkste voordeel: AI-responses die automatisch worden geparsed naar Python objects.

## 4. Praktische voorbeelden

### Basis voorbeeld: Eenvoudige string response
```python
from pydantic_ai import Agent

# Maak een eenvoudige agent
agent = Agent('openai:gpt-4')

# Synchrone call
result = agent.run_sync('Wat is de hoofdstad van Nederland?')
print(result.data)  # "Amsterdam"
```

### Gestructureerde output met Pydantic models
```python
from pydantic import BaseModel
from pydantic_ai import Agent

class CityInfo(BaseModel):
    name: str
    country: str
    population: int
    founded_year: int

# Agent met gestructureerde output
agent = Agent('openai:gpt-4', result_type=CityInfo)

result = agent.run_sync('Geef informatie over Amsterdam')
city = result.data
print(f"{city.name} werd opgericht in {city.founded_year}")
print(f"Populatie: {city.population:,}")
```

### System prompts en context
```python
from pydantic import BaseModel
from pydantic_ai import Agent

class Recipe(BaseModel):
    name: str
    ingredients: list[str]
    instructions: list[str]
    prep_time_minutes: int

# Agent met system prompt
agent = Agent(
    'openai:gpt-4',
    result_type=Recipe,
    system_prompt='Je bent een professionele chef. Geef altijd praktische, haalbare recepten.'
)

result = agent.run_sync('Maak een recept voor pasta carbonara')
recipe = result.data
print(f"Recept: {recipe.name}")
print(f"Bereidingstijd: {recipe.prep_time_minutes} minuten")
```

### Dependencies en Tools
```python
from pydantic import BaseModel
from pydantic_ai import Agent, RunContext

class WeatherInfo(BaseModel):
    location: str
    temperature: float
    description: str

def get_weather(location: str) -> dict:
    # Simuleer weather API call
    return {
        "location": location,
        "temperature": 20.5,
        "description": "Partly cloudy"
    }

# Agent met tools
agent = Agent(
    'openai:gpt-4',
    result_type=WeatherInfo,
    tools=[get_weather]
)

result = agent.run_sync('Wat is het weer in Amsterdam?')
weather = result.data
print(f"Het is {weather.temperature}°C in {weather.location}")
```

### Error handling
```python
from pydantic_ai import Agent
from pydantic_ai.exceptions import ModelRetryError

agent = Agent('openai:gpt-4')

try:
    result = agent.run_sync('Wat is de hoofdstad van Nederland?')
    print(result.data)
except ModelRetryError as e:
    print(f"AI model fout: {e}")
except Exception as e:
    print(f"Onverwachte fout: {e}")
```

## 5. Best practices

### 1. Gebruik duidelijke Pydantic models
```python
from pydantic import BaseModel, Field

class ProductReview(BaseModel):
    product_name: str = Field(description="De naam van het product")
    rating: int = Field(ge=1, le=5, description="Rating van 1-5 sterren")
    pros: list[str] = Field(description="Positieve aspecten")
    cons: list[str] = Field(description="Negatieve aspecten")
    recommendation: bool = Field(description="Of het product wordt aanbevolen")
```

### 2. Gebruik system prompts voor consistentie
```python
agent = Agent(
    'openai:gpt-4',
    result_type=ProductReview,
    system_prompt='''
    Je bent een objectieve productrecensent. 
    Geef eerlijke, uitgebalanceerde reviews.
    Gebruik concrete voorbeelden en vermijd overdreven taal.
    '''
)
```

### 3. Test je agents
```python
def test_city_agent():
    agent = Agent('openai:gpt-4', result_type=CityInfo)
    result = agent.run_sync('Informatie over Parijs')
    
    assert result.data.name == "Paris"
    assert result.data.country == "France"
    assert result.data.population > 2000000
```

## 6. Veelvoorkomende use cases

| Use case | Beschrijving | Voorbeeld output type |
|----------|-------------|----------------------|
| Data extractie | Haal gestructureerde data uit tekst | `ContactInfo`, `InvoiceData` |
| Content classificatie | Categoriseer content automatisch | `CategoryClassification` |
| Sentiment analyse | Analyseer sentiment in tekst | `SentimentAnalysis` |
| Code generatie | Genereer code met metadata | `CodeSolution` |
| Vraag & antwoord | Beantwoord vragen met bronnen | `AnswerWithSources` |

## Volgende stappen
- Probeer de voorbeelden in `TRYME.py`
- Maak de oefeningen in `MAKEME.md`
- Experimenteer met verschillende AI-providers
- Bouw je eigen gestructureerde AI-applicatie

## Nuttige links
- [Pydantic AI Documentatie](https://ai.pydantic.dev/)
- [Pydantic Documentatie](https://docs.pydantic.dev/)
- [OpenAI API Documentatie](https://platform.openai.com/docs/)