# Object Detection Setup Guide

## Quick Start

### 2. Maak Test Content

```bash
# Maak een test video met stoel
python create_chair_video.py

# Of alleen een test afbeelding
python create_chair_video.py --image
```

### 3. Test Object Detection

```bash
# Test met afbeelding
python TRYME.py --input chair_test.jpg --save-image

# Test met video
python TRYME.py --input chair_video.mp4 --output result.mp4

# Test met webcam (als beschikbaar)
python TRYME.py --input webcam
```

## Troubleshooting

### Probleem: "transformers niet geïnstalleerd"
**Oplossing:**
```bash
pip install transformers torch
```

### Probleem: "CUDA not available"
**Info:** Dit is normaal als je geen NVIDIA GPU hebt. Het model werkt ook op CPU, alleen langzamer.

### Probleem: "FFmpeg not found"
**Oplossing:**
```bash
# Ubuntu/Debian
sudo apt install ffmpeg

# macOS
brew install ffmpeg

# Windows
# Download van https://ffmpeg.org/
```

### Probleem: "Webcam kan niet worden geopend"
**Mogelijke oplossingen:**
- Controleer of webcam in gebruik is door andere app
- Probeer een andere camera index: wijzig `cv2.VideoCapture(0)` naar `cv2.VideoCapture(1)`
- Test webcam met andere software eerst

### Probleem: "Memory error" of crash
**Oplossingen:**
- Gebruik kleinere video's voor testen
- Verhoog frame skip: `if frame_count % 10 == 0:` (proces minder frames)
- Sluit andere memory-intensieve applicaties

## Voorbeelden

### Basis Usage
```bash
# Simpel - detecteer in afbeelding
python TRYME.py --input photo.jpg

# Met lage confidence threshold
python TRYME.py --input video.mp4 --confidence 0.5

# Webcam met opslaan
python TRYME.py --input webcam --output webcam_recording.mp4
```

### Custom Scenarios
```python
# In je eigen code:
from TRYME import SimpleObjectDetector

detector = SimpleObjectDetector(confidence_threshold=0.7)
detections = detector.detect_objects(pil_image)

for detection in detections:
    print(f"Found: {detection['label']} ({detection['confidence']:.2f})")
```

## Performance Tips

### Voor Snellere Processing:
1. **Lagere resolutie**: Resize video's naar 640x480
2. **Frame skipping**: Process elke 3e of 5e frame
3. **Hogere confidence**: Gebruik threshold 0.8+ om false positives te verminderen
4. **Batch processing**: Voor grote video's, proces in chunks

### Voor Betere Accuraatheid:
1. **Lagere confidence**: Gebruik threshold 0.5-0.6
2. **Hogere resolutie**: Behoud originele video kwaliteit
3. **Process alle frames**: Geen frame skipping
4. **Multi-model ensemble**: Combineer meerdere modellen

## Supported Formats

### Input Formaten:
- **Images**: JPG, PNG, BMP, TIFF
- **Videos**: MP4, AVI, MOV, MKV, WEBM
- **Live**: Webcam, IP camera streams

### Output Formaten:
- **Videos**: MP4 (H.264)
- **Images**: JPG, PNG

## Hardware Requirements

### Minimum:
- CPU: Dual-core 2GHz+
- RAM: 4GB+
- Storage: 2GB free space

### Aanbevolen:
- CPU: Quad-core 3GHz+
- RAM: 8GB+
- GPU: NVIDIA GTX 1060+ of equivalente AMD
- Storage: SSD voor snellere I/O

### Voor Real-time Processing:
- GPU met CUDA ondersteuning
- 16GB+ RAM
- Fast SSD storage

## Meer Modellen

### Different Detection Approaches:

**1. PyTorch + Transformers (default)**
```python
# DETR models (current approach)
detector = SimpleObjectDetector("facebook/detr-resnet-50")
```

**2. Ultralytics YOLO (simplest)**  
```python
from ultralytics import YOLO
model = YOLO("yolov8n.pt")
results = model("image.jpg")
```

**3. TensorFlow Hub**
```python
import tensorflow_hub as hub
model = hub.load("https://tfhub.dev/tensorflow/ssd_mobilenet_v2/2")
```

**4. OpenCV DNN (lightweight)**
```python
net = cv2.dnn.readNet("yolov4.weights", "yolov4.cfg")
```

### Framework Comparison:
| Framework | Setup | Speed | Accuracy | Memory | Learning Curve |
|-----------|--------|-------|----------|--------|----------------|
| Ultralytics | ⚡⚡⚡ | ⚡⚡⚡ | ⭐⭐⭐ | 🔋🔋 | Easy |
| OpenCV DNN | ⚡⚡ | ⚡⚡⚡ | ⭐⭐ | 🔋 | Medium |
| TensorFlow | ⚡⚡ | ⚡⚡ | ⭐⭐⭐ | 🔋🔋 | Medium |
| PyTorch | ⚡ | ⚡⚡ | ⭐⭐⭐⭐ | 🔋🔋🔋 | Advanced |

## Next Steps

1. **Experimenteer** met verschillende modellen en settings
2. **Probeer** eigen video's en afbeeldingen
3. **Optimaliseer** voor jouw specifieke use case
4. **Bouw** custom detection pipelines
5. **Integreer** in grotere applicaties

Voor vragen: check de MAKEME.md voor oefeningen en voorbeelden!