# GitHub Copilot

GitHub Copilot is een AI-aangedreven code-assistent die direct in je editor werkt. In dit hoofdstuk leer je hoe je Copilot effectief kunt gebruiken voor Python-ontwikkeling, van eenvoudige code completion tot complexe refactoring.

## Inhoud
1. Wat is GitHub Copilot?
2. Toegang
3. Effectief gebruik van Copilot
4. Best practices en tips
5. Copilot vs andere AI-tools

---

## 1. Wat is GitHub Copilot?

GitHub Copilot is een AI pair programmer ontwikkeld door GitHub in samenwerking met OpenAI. Het gebruikt een speciaal getraind model (gebaseerd op GPT) dat is getraind op publieke code repositories.

**Kernfunctionaliteiten:**
- **Code completion**: Suggereert code terwijl je typt
- **Functie generatie**: Schrijft hele functies op basis van comments of functienamen
- **Test generatie**: Genereert unit tests voor bestaande code
- **Code uitleg**: Legt complexe code uit in gewoon Nederlands
- **Refactoring**: Helpt bij het verbeteren van bestaande code
- **Documentatie**: Genereert docstrings en comments

## 2. Toegang verkrijgen
- Account aanmaken op github.com
- Copilot activeren in je GitHub account settings
- Editor extension installeren (VS Code, JetBrains, Vim, etc.)

## 3. Effectief gebruik van Copilot

### 3.1 Code Completion
Copilot suggereert code automatisch terwijl je typt:

```python
# Type gewoon de functienaam en docstring:
def calculate_fibonacci(n):
    """Calculate the nth Fibonacci number."""
    # Copilot suggereert automatisch de implementatie
```

**Tips:**
- Schrijf duidelijke functienamen en docstrings
- Begin met comments die je intentie beschrijven
- Gebruik Tab om suggesties te accepteren
- Gebruik Alt+] / Alt+[ om door suggesties te navigeren

### 3.2 Chat functionaliteit
In VS Code kun je Copilot Chat gebruiken voor interactieve hulp:

```
# In Copilot Chat kun je vragen stellen zoals:
"Hoe kan ik deze functie optimaliseren voor grote datasets?"
"Schrijf unit tests voor deze klasse"
"Leg deze regex uit"
"Refactor deze code naar object-oriented style"
```

### 3.3 Specifieke commando's
Copilot Chat ondersteunt specifieke slash-commando's:

| Commando | Functie | Voorbeeld |
|----------|---------|-----------|
| `/explain` | Leg code uit | `/explain wat doet deze functie?` |
| `/fix` | Repareer bugs | `/fix deze error in mijn code` |
| `/tests` | Genereer tests | `/tests voor deze klasse` |
| `/doc` | Schrijf documentatie | `/doc voor deze API` |

## 4. Best practices en tips

### 4.1 Schrijf goede prompts
```python
# GOED: Duidelijke intentie
def validate_email_address(email):
    """
    Validate email address using regex.
    Returns True if valid, False otherwise.
    """
    # Copilot genereert nu relevante code

# MINDER GOED: Vage functienaam
def check(data):
    # Copilot weet niet wat je wilt checken
```

### 4.2 Gebruik context
```python
# Geef context door imports en eerdere code
import pandas as pd
import numpy as np

# Nu weet Copilot dat je met data science werkt
def clean_dataset(df):
    """Remove missing values and outliers from pandas DataFrame."""
    # Suggereert pandas-specifieke code
```

### 4.3 Iteratief werken
1. Begin met een comment of functiesignature
2. Laat Copilot een eerste versie genereren
3. Verfijn en verbeter incrementeel
4. Test regelmatig

### 4.4 Code review blijft essentieel
```python
# Controleer altijd Copilot suggesties:
def divide_numbers(a, b):
    # Copilot suggereert misschien:
    return a / b
    
    # Maar je moet zelf aan edge cases denken:
    # if b == 0:
    #     raise ValueError("Cannot divide by zero")
    # return a / b
```

## 5. Copilot vs andere AI-tools

| Tool | Sterke punten | Zwakke punten | Wanneer gebruiken |
|------|---------------|---------------|-------------------|
| **GitHub Copilot** | Editor integratie, context aware | Beperkte reasoning | Dagelijkse ontwikkeling |
| **ChatGPT/Claude** | Uitgebreide uitleg, complex reasoning | Geen editor integratie | Conceptuele vragen, debugging |
| **Cursor/Aider** | Hele bestanden editen | Minder mainstream | Grote refactoring taken |
