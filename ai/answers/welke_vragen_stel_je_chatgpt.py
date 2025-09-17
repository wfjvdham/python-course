"""Antwoorden / voorbeelduitwerkingen voor de programmeergerichte prompts.

Let op: Dit zijn voorbeeldprompts, geen 'enige juiste' antwoorden. Doel is structuur + duidelijkheid.
"""

debug_prompt = (
    "Context: Ik heb een functie die een lijst van ints verwerkt, maar ik krijg een TypeError: 'int' object is not iterable in regel 18. "
    "Code (vereenvoudigd):\n\n"
    "def process(values):\n    total = 0\n    for v in values:\n        for x in v:  # fout?\n            total += x\n    return total\n\n"
    "Vraag: Leg uit waarom deze fout ontstaat en geef 2 correcte alternatieven. "
    "Outputvorm: Eerst analyse, daarna codeblokken."
)

refactor_prompt = (
    "Context: Drie bijna identieke if-else blokken die alleen op key naam verschillen. "
    "Code: settings = {}; if 'host' in cfg: settings['host']=cfg['host']; if 'port' in cfg: settings['port']=int(cfg['port']); if 'debug' in cfg: settings['debug']=bool(cfg['debug']). "
    "Vraag: Geef een Pythonic refactor zonder herhaling, liefst uitbreidbaar."
)

performance_prompt = (
    "Context: Ik laad een 500MB CSV met pandas.read_csv en daarna doe ik meerdere filter passes. "
    "Vraag: Geef optimalisaties (kolommen selecteren, dtypes, chunks, categoricals) en wanneer elke geschikt is. "
    "Outputvorm: Tabel met maatregel | effect | trade-off."
)

tests_prompt = (
    "Context: Functie normalize(names: list[str]) -> list[str] lowercased, strip spaties en verwijdert duplicates behoudt originele volgorde. "
    "Vraag: Schrijf pytest tests: normaal geval, lege lijst, alleen spaties, duplicates met case-verschillen, niet-string waardes (verwachte gedrag)."
)

uitleg_prompt = (
    "Vraag: Leg uit waarom een generator minder geheugen gebruikt dan een lijst comprehension bij het verwerken van miljoenen items. "
    "Eisen: Geef analogie + klein codevoorbeeld + memory verschil beschrijving (kwalitatief)."
)

edge_cases_prompt = (
    "Context: Ik parse JSON user-profielen met optionele velden: email, phone, roles (lijst), created_at (ISO), preferences (dict). "
    "Vraag: Noem minstens 8 edge cases die fouten kunnen veroorzaken + korte mitigatie."
)

alternatieven_prompt = (
    "Context: Ik gebruik open('file.txt').read() en vergeet soms close(). "
    "Vraag: Geef modernere alternatieven (with-statement, pathlib, contextlib) met kort voorbeeld en wanneer welke handig is."
)

architectuur_prompt = (
    "Context: Ik bouw nu een CLI-tool maar wil later een REST API toevoegen. "
    "Vraag: Stel een map- en module-structuur voor (layers: core/domain/adapters/cli) + korte uitleg per laag."
)

docstring_prompt = (
    "Vraag: Geef een Google style docstring template voor validate(data: dict) -> list[str] die validatiefouten teruggeeft, inclusief raises sectie."
)

review_prompt = (
    "Context: Ik wil een code review. Ik lever straks een snippet aan. "
    "Vraag: Geef beoordelingscriteria (complexiteit, SRP, naming, side-effects) en vraag me daarna om de code te plakken. Geen herschrijf tot ik dat vraag."
)

bonus_prompt = (
    "Context: Functie laad CSV -> filter -> transform -> output json. Performance matig, code duplicatie, geen tests. "
    "Vraag: 1) Analyseer problemen 2) Geef refactorstrategie 3) Schrijf 3 pytest tests 4) Geef mogelijke performance winst ideeën. "
    "Outputvorm: Genummerde secties."
)

alle_prompts = [
    debug_prompt,
    refactor_prompt,
    performance_prompt,
    tests_prompt,
    uitleg_prompt,
    edge_cases_prompt,
    alternatieven_prompt,
    architectuur_prompt,
    docstring_prompt,
    review_prompt,
    bonus_prompt,
]

if __name__ == "__main__":
    for i, p in enumerate(alle_prompts, 1):
        print(f"Voorbeeldprompt {i}:\n{p}\n{'-'*40}")
