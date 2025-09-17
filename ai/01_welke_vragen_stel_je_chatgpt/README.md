
# Welke vragen stel je ChatGPT?

In dit hoofdstuk leer je welke soorten programmeervragen je aan ChatGPT kunt stellen om sneller te leren, fouten op te sporen en betere code te schrijven. We richten ons nu specifiek op softwareontwikkeling.

## Inhoud
1. Categorieën programmeervragen
2. Tips voor effectieve code-prompts
3. Voorbeeldprompts per categorie
4. Oefeningen

---

## 1. Categorieën programmeervragen

| Categorie | Wanneer gebruiken | Voorbeeldvraag |
|-----------|------------------|----------------|
| Conceptuitleg | Als je theorie wilt begrijpen | "Leg in simpele taal uit wat een iterator is in Python." |
| Debugging | Als je foutmeldingen of vreemd gedrag ziet | "Ik krijg een ValueError in regel 42, kun je uitleggen waarom?" |
| Refactoren | Als je code werkt maar leesbaarder/DRYer kan | "Hoe kan ik deze dubbele if-blokken eleganter maken?" |
| Alternatieven | Als je een andere aanpak zoekt | "Is er een Pythonic manier om deze for-loop te vervangen?" |
| Performance | Als code traag is | "Deze functie op grote lijsten duurt 5s. Hoe kan ik profileren en versnellen?" |
| Testing | Voor het schrijven of verbeteren van tests | "Schrijf pytest tests voor deze functie met edge cases." |
| API / Library gebruik | Als je een onbekende lib gebruikt | "Hoe gebruik ik pathlib om recursief .csv-bestanden te vinden?" |
| Documentatie / Naming | Voor beter onderhoud | "Kun je een duidelijke docstring-sjabloon geven voor deze klasse?" |
| Architectuur / Design | Voor grotere structuurvragen | "Wanneer kies ik voor een Strategy pattern in plaats van if/elif?" |
| Genereren van voorbeelden | Voor snelle start | "Geef een minimal werkend voorbeeld van async HTTP requests met aiohttp." |

## 2. Tips voor effectieve code-prompts

- Geef relevante code mee (maar knip irrelevante delen weg).
- Benoem duidelijk: DOEL (wat wil je bereiken) + CONTEXT (omgeving, versie) + PROBLEEM (fout/gedrag) + VERWACHT RESULTAAT.
- Vraag om meerdere opties: "Geef 2 benaderingen + voor- en nadelen." 
- Vraag naar edge cases: "Mis ik randgevallen?" 
- Structureer grotere vragen met bullets.
- Voeg constraints toe: performance, leesbaarheid, compatibiliteit.
- Vraag om uitleg vóór of na code: "Eerst uitleg, dan code." of "Alleen code zonder extra tekst." afhankelijk van je doel.

Template:

```
Context: (korte beschrijving)
Code: (relevant fragment)
Vraag: (concreet wat je wilt)
Criteria: (optioneel: snel / leesbaar / Python 3.11 / geen externe libs)
Outputvorm: (bijv. alleen code / stappenplan / tabel)
```

## 3. Voorbeeldprompts per categorie

**Conceptuitleg:**
> Leg in 5 zinnen uit wat een generator is in Python en wanneer je het gebruikt.

**Debugging (met foutmelding):**
```
Ik krijg deze fout:
Traceback (most recent call last):
	File "main.py", line 12, in <module>
		process(data)
	File "main.py", line 5, in process
		return sum(x.value for x in data)
AttributeError: 'int' object has no attribute 'value'
Wat veroorzaakt dit en hoe los ik het op?
```

**Refactor:**
> Kun je deze code herschrijven naar een versie zonder geneste ifs, maar wel duidelijk?

**Performance:**
> Deze functie doet 1 miljoen dictionary lookups en voelt traag. Welke optimalisaties kan ik proberen? Ik werk in Python 3.11.

**Tests:**
> Schrijf pytest-tests voor deze functie met ten minste: normaal pad, lege invoer, foutscenario.

**Architectuur:**
> Ik twijfel tussen een Factory pattern en eenvoudige if-else logica voor het maken van verschillende exportformatters (csv/json/xml). Wanneer is een pattern gerechtvaardigd hier?

**Edge cases check:**
> Mis ik randgevallen in deze functie die een lijst normaliseert naar unieke, gesorteerde strings?

## 5. Oefeningen

Zie het bestand `MAKEME.md` voor oefeningen bij dit hoofdstuk.
