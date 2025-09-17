# Programmeergerichte voorbeeldprompts voor ChatGPT

prompts = [
    # Debugging
    "Context: Python functie crasht met TypeError: 'NoneType' object is not iterable. Codefragment volgt. Vraag: Leg uit oorzaak + geef 2 oplossingen.",
    # Refactor
    "Context: Functie met 3 bijna identieke for-loops over verschillende lijsten. Vraag: Hoe samenvoegen zonder leesbaarheid te verliezen?",
    # Performance
    "Context: Pandas DataFrame (2M rijen) -> groupby + apply is traag. Vraag: Alternatieven + wanneer vectoriseren beter is.",
    # Tests
    "Context: Functie 'slugify(text)' moet spaties vervangen door '-' en lowercase maken. Vraag: Schrijf 4 pytest cases incl. edge case unicode.",
    # Uitleg
    "Vraag: Leg kort verschil uit tussen list comprehension en generator expression + geheugenimplicaties.",
    # Architectuur
    "Context: CLI-tool die later web-API kan worden. Vraag: Mapstructuur voorstel + waarom scheiding domain/adapters nuttig is.",
    # Edge cases
    "Context: Parser leest JSON config. Vraag: Noem 8 edge cases (types, ontbrekende keys, encoding) + hoe af te vangen.",
    # Documentatie
    "Vraag: Geef een Google style docstring template voor 'load_users(path: str) -> list[User]'.",
]

for i, p in enumerate(prompts, 1):
    print(f"Prompt {i}: {p}")
