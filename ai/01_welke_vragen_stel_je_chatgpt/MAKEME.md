# Oefeningen: Programmeervragen aan ChatGPT

Formuleer de juiste prompts. Zorg dat elke prompt voldoende context bevat en een duidelijke gewenste output.

1. Debugging: Je krijgt een `TypeError` in een functie die een lijst van ints verwerkt. Formuleer een prompt om ChatGPT te laten helpen de oorzaak te vinden.
2. Refactor: Je hebt een functie met 3 herhaalde if-else blokken die alleen een sleutelnaam verschillen. Vraag om een Pythonic refactor.
3. Performance: Je script leest een groot CSV-bestand (500MB) en is traag. Maak een prompt om optimalisaties/aanpak te vragen.
4. Testen: Je hebt een functie `def normalize(names: list[str]) -> list[str]:` die strings lowercased, strip’t en duplicate verwijdert. Vraag om pytest tests inclusief randgevallen.
5. Uitleg: Je begrijpt niet waarom een generator minder geheugen gebruikt dan een lijst. Formuleer een prompt die om uitleg mét voorbeeld vraagt.
6. Edge cases: Je hebt code die JSON inleest en optional velden verwerkt. Vraag ChatGPT om randgevallen die je misschien vergeet.
7. Alternatieven: Je gebruikt handmatig `open()` + `read()` + `close()`. Vraag om modernere of veiligere alternatieven met korte uitleg.
8. Architectuur: Je bouwt een CLI-tool die later een web-API kan worden. Vraag om een structuur die toekomstige uitbreiding makkelijk maakt.
9. Documentatie: Vraag om een voorbeeld van een goede docstring (Google style) voor een functie die data valideert en errors verzamelt.
10. Review: Formuleer een prompt waarmee je ChatGPT vraagt om een kritisch code review op leesbaarheid, complexiteit en naming (zonder het herschrijven unless gevraagd).

Bonus: Combineer meerdere aspecten (bijv. refactor + tests + performance) in één goed gestructureerde super-prompt.
