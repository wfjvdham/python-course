# Oefeningen: Object Detection in Video's

## Opdracht 1: Basis Object Detection
**Duur: 30 minuten**

Maak een script dat:
1. Een afbeelding inlaadt
2. Alle objecten detecteert met een confidence > 0.8
3. De resultaten print in een nette tabel
4. Een geannoteerde afbeelding opslaat

```python
# Verwacht output formaat:
"""
Gedetecteerde objecten:
+----------+------------+------------------+
| Object   | Confidence | Positie (x,y,w,h)|
+----------+------------+------------------+
| person   | 0.95       | (100,50,200,400) |
| chair    | 0.87       | (300,200,150,180)|
+----------+------------+------------------+
"""
```

## Opdracht 2: Video Object Counter
**Duur: 45 minuten**

Bouw een video analyzer die:
1. Een video inlaadt (`chair_video.mp4`)
2. Elke 10e frame analyseert
3. Het aantal unieke objecten per categorie telt
4. Een samenvattingsrapport genereert

**Bonus punten:**
- Maak een grafiek van object tellingen over tijd
- Detecteer wanneer een nieuw object in beeld komt

## Opdracht 3: Real-time Chair Detector
**Duur: 60 minuten**

Ontwikkel een applicatie die:
1. De webcam gebruikt als input
2. Real-time stoelen detecteert
3. Een alarm geeft wanneer meer dan 3 stoelen zichtbaar zijn
4. Screenshots opslaat van interessante detecties

**Extra uitdaging:**
- Voeg een GUI toe met tkinter of streamlit
- Implementeer object tracking tussen frames

## Opdracht 4: Custom Object Filter
**Duur: 45 minuten**

Maak een configureerbaar detection system:
1. Lees een config file met gewenste object types
2. Process een video en filter alleen die objecten
3. Genereer een highlight reel met alleen relevante scenes
4. Maak statistieken per tijdsegment

**Config voorbeeld:**
```json
{
  "target_objects": ["person", "chair", "laptop"],
  "min_confidence": 0.75,
  "scene_duration": 5.0,
  "output_format": "mp4"
}
```

## Opdracht 5: Performance Benchmark
**Duur: 30 minuten**

Vergelijk verschillende optimalisatie strategieën:
1. Test verschillende frame skip rates (1, 2, 5, 10)
2. Test verschillende input resoluties (320p, 480p, 720p)
3. Meet processing tijd per frame
4. Maak een performance rapport

**Meetpunten:**
- FPS processing rate
- Memory usage
- Detection accuracy (subjective)
- Total processing time

## Opdracht 6: Multi-model Comparison
**Duur: 90 minuten**

Implementeer en vergelijk verschillende modellen:
1. DETR (facebook/detr-resnet-50)
2. YOLO (ultraltics/yolov5)
3. Een ander model naar keuze

**Vergelijkingscriteria:**
- Accuracy op test video
- Processing speed
- Memory usage
- Ease of implementation

## Bonus Opdracht: Smart Home Security
**Duur: 120 minuten**

Bouw een smart security system:
1. Monitor meerdere camera feeds (simuleer met video files)
2. Detecteer ongewone activiteit (personen op onverwachte tijden)
3. Stuur notificaties bij verdachte detecties
4. Maak een dashboard met live feeds en alerts

**Features:**
- Multi-threading voor meerdere streams
- Database logging van events
- Email/SMS notificaties
- Web interface voor monitoring

## Tips voor alle opdrachten

### Performance
- Begin altijd met kleine test video's
- Monitor je memory usage
- Test op verschillende hardware als mogelijk

### Debugging
- Print tussenresultaten bij problemen
- Gebruik `matplotlib` om bounding boxes te visualiseren
- Log processing tijden per stap

### Code kwaliteit
- Schrijf docstrings voor je functies
- Gebruik type hints waar mogelijk
- Maak je code modulair en herbruikbaar

### Testing
- Test met verschillende video resoluties
- Probeer video's met veel/weinig objecten
- Test edge cases (donkere video's, snelle bewegingen)

## Inleveren

Voor elke opdracht:
1. Werkende Python code (.py files)
2. Requirements.txt met dependencies
3. README.md met uitleg en gebruiksinstructies
4. Test resultaten/screenshots
5. Korte reflectie op moeilijkheden en learnings

## Evaluatiecriteria

- **Functionaliteit** (40%): Werkt de code zoals gevraagd?
- **Code kwaliteit** (30%): Clean, readable, documented code?
- **Performance** (20%): Efficient gebruik van resources?
- **Creativiteit** (10%): Innovatieve toevoegingen of oplossingen?

---

*Veel succes! Vergeet niet om regelmatig te committen naar git en je vorderingen te documenteren.*