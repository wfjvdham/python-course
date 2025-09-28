# Object Detection in Video's

Dit hoofdstuk legt uit hoe je objecten kunt detecteren in video's met behulp van moderne AI-modellen. We behandelen verschillende benaderingen: van PyTorch + Transformers voor cutting-edge modellen tot lightweight alternatieven met OpenCV en Ultralytics YOLO.

## Inhoud
1. Wat is object detection?
2. Installatie en setup
3. Object detection in afbeeldingen
4. Object detection in video's
5. Praktische voorbeelden
6. Oefeningen

---

## 1. Wat is object detection?

Object detection is een computer vision taak waarbij we:
- **Objecten identificeren**: Wat zien we in de afbeelding/video?
- **Locaties bepalen**: Waar bevinden de objecten zich?
- **Bounding boxes**: Rechthoekige kaders rond gedetecteerde objecten
- **Confidence scores**: Hoe zeker is het model van de detectie?

### Populaire object detection modellen

| Model | Voordelen | Nadelen | Gebruik |
|-------|-----------|---------|---------|
| YOLO (You Only Look Once) | Snel, real-time | Minder accuraat voor kleine objecten | Video surveillance, real-time apps |
| DETR (Detection Transformer) | Zeer accuraat, end-to-end | Langzamer | High-quality detection, research |
| SSD (Single Shot Detector) | Goede balans snelheid/accuraatheid | Complexere setup | Mobile apps, embedded systems |

## 2. Installatie en setup

### Optie 1: PyTorch + Transformers (standaard, meest flexibel)
```bash
# Via pyproject.toml (aanbevolen)
pip install -e .

# Of direct:
pip install transformers torch torchvision opencv-python pillow matplotlib numpy
```

### Optie 2: Ultralytics YOLO (eenvoudigst)
```bash
pip install ultralytics opencv-python
```

### Optie 3: TensorFlow (productie-klaar)
```bash  
pip install tensorflow tensorflow-hub opencv-python
```

### Optie 4: OpenCV DNN (minimale dependencies)
```bash
pip install opencv-python numpy
```

**Waarom PyTorch als standaard?**
- **Hugging Face ecosysteem**: Grootste collectie pre-trained modellen
- **Moderne architecturen**: DETR, Vision Transformers
- **Onderzoek-vriendelijk**: Eenvoudig om te experimenteren
- **Flexibiliteit**: Dynamische computational graphs
- **Community**: Actieve ontwikkeling en ondersteuning

## 3. Object detection in afbeeldingen

### Basis voorbeeld met DETR

```python
from transformers import DetrImageProcessor, DetrForObjectDetection
import torch
from PIL import Image, ImageDraw
import matplotlib.pyplot as plt

# Model en processor laden
processor = DetrImageProcessor.from_pretrained("facebook/detr-resnet-50")
model = DetrForObjectDetection.from_pretrained("facebook/detr-resnet-50")

def detect_objects_in_image(image_path, confidence_threshold=0.9):
    """
    Detecteer objecten in een afbeelding
    
    Args:
        image_path: pad naar de afbeelding
        confidence_threshold: minimum confidence voor detectie
    
    Returns:
        list: gedetecteerde objecten met bounding boxes
    """
    # Afbeelding laden
    image = Image.open(image_path)
    
    # Preprocessing
    inputs = processor(images=image, return_tensors="pt")
    
    # Inference
    with torch.no_grad():
        outputs = model(**inputs)
    
    # Postprocessing
    target_sizes = torch.tensor([image.size[::-1]])
    results = processor.post_process_object_detection(
        outputs, target_sizes=target_sizes, threshold=confidence_threshold
    )[0]
    
    # Resultaten formatteren
    detections = []
    for score, label, box in zip(results["scores"], results["labels"], results["boxes"]):
        detections.append({
            "label": model.config.id2label[label.item()],
            "confidence": score.item(),
            "box": box.tolist()  # [x_min, y_min, x_max, y_max]
        })
    
    return detections, image

def visualize_detections(image, detections):
    """Visualiseer detecties op de afbeelding"""
    draw = ImageDraw.Draw(image)
    
    for detection in detections:
        box = detection["box"]
        label = detection["label"]
        confidence = detection["confidence"]
        
        # Bounding box tekenen
        draw.rectangle(box, outline="red", width=3)
        
        # Label en confidence tekenen
        text = f"{label}: {confidence:.2f}"
        draw.text((box[0], box[1] - 20), text, fill="red")
    
    return image

# Voorbeeld gebruik
if __name__ == "__main__":
    # Detecteer objecten
    detections, image = detect_objects_in_image("example_image.jpg")
    
    # Visualiseer resultaten
    result_image = visualize_detections(image.copy(), detections)
    
    # Toon resultaat
    plt.figure(figsize=(12, 8))
    plt.imshow(result_image)
    plt.axis('off')
    plt.title(f"Gedetecteerd: {len(detections)} objecten")
    plt.show()
    
    # Print detecties
    for i, detection in enumerate(detections):
        print(f"{i+1}. {detection['label']}: {detection['confidence']:.3f}")
```

## 4. Object detection in video's

### Real-time video processing

```python
import cv2
import numpy as np
from transformers import DetrImageProcessor, DetrForObjectDetection
import torch
from PIL import Image

class VideoObjectDetector:
    def __init__(self, model_name="facebook/detr-resnet-50", confidence_threshold=0.8):
        """
        Video object detector met DETR model
        
        Args:
            model_name: Hugging Face model naam
            confidence_threshold: minimum confidence voor detectie
        """
        self.processor = DetrImageProcessor.from_pretrained(model_name)
        self.model = DetrForObjectDetection.from_pretrained(model_name)
        self.confidence_threshold = confidence_threshold
        
        # GPU ondersteuning
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model.to(self.device)
        
    def detect_frame(self, frame):
        """Detecteer objecten in een enkele frame"""
        # OpenCV (BGR) naar PIL (RGB)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        pil_image = Image.fromarray(rgb_frame)
        
        # Preprocessing
        inputs = self.processor(images=pil_image, return_tensors="pt")
        inputs = {k: v.to(self.device) for k, v in inputs.items()}
        
        # Inference
        with torch.no_grad():
            outputs = self.model(**inputs)
        
        # Postprocessing
        target_sizes = torch.tensor([pil_image.size[::-1]]).to(self.device)
        results = self.processor.post_process_object_detection(
            outputs, target_sizes=target_sizes, threshold=self.confidence_threshold
        )[0]
        
        return results
    
    def draw_detections(self, frame, results):
        """Teken detecties op frame"""
        for score, label, box in zip(results["scores"], results["labels"], results["boxes"]):
            # Bounding box coordinaten
            x1, y1, x2, y2 = map(int, box.cpu().numpy())
            
            # Label en confidence
            label_name = self.model.config.id2label[label.item()]
            confidence = score.item()
            
            # Tekenen
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame, f"{label_name}: {confidence:.2f}", 
                       (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        
        return frame
    
    def process_video(self, video_path, output_path=None, skip_frames=2):
        """
        Process een complete video
        
        Args:
            video_path: pad naar input video
            output_path: pad voor output video (optioneel)
            skip_frames: aantal frames om over te slaan (voor performance)
        """
        cap = cv2.VideoCapture(video_path)
        
        # Video eigenschappen
        fps = int(cap.get(cv2.CAP_PROP_FPS))
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        
        # Output video writer
        if output_path:
            fourcc = cv2.VideoWriter_fourcc(*'mp4v')
            out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))
        
        frame_count = 0
        
        try:
            while True:
                ret, frame = cap.read()
                if not ret:
                    break
                
                # Skip frames voor performance
                if frame_count % (skip_frames + 1) == 0:
                    # Object detection
                    results = self.detect_frame(frame)
                    frame = self.draw_detections(frame, results)
                
                # Toon frame
                cv2.imshow('Object Detection', frame)
                
                # Opslaan als gewenst
                if output_path:
                    out.write(frame)
                
                # Stoppen met 'q'
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
                
                frame_count += 1
                
        finally:
            # Cleanup
            cap.release()
            if output_path:
                out.release()
            cv2.destroyAllWindows()

# Voorbeeld gebruik
if __name__ == "__main__":
    # Detector initialiseren
    detector = VideoObjectDetector(confidence_threshold=0.7)
    
    # Video verwerken
    detector.process_video("chair_video.mp4", "output_with_detections.mp4")
```

## 5. Praktische voorbeelden

### Specifieke objecten detecteren

```python
def detect_chairs_only(image_path):
    """Detecteer alleen stoelen in een afbeelding"""
    detections, image = detect_objects_in_image(image_path, confidence_threshold=0.7)
    
    # Filter alleen stoelen
    chairs = [d for d in detections if d["label"].lower() == "chair"]
    
    print(f"Gevonden {len(chairs)} stoelen:")
    for i, chair in enumerate(chairs):
        print(f"  Stoel {i+1}: confidence {chair['confidence']:.3f}")
    
    return chairs, image

def count_objects_in_video(video_path, target_objects=None):
    """Tel objecten in een video"""
    if target_objects is None:
        target_objects = ["person", "chair", "car", "bicycle"]
    
    detector = VideoObjectDetector()
    cap = cv2.VideoCapture(video_path)
    
    object_counts = {obj: 0 for obj in target_objects}
    frame_count = 0
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        # Process elke 30e frame
        if frame_count % 30 == 0:
            results = detector.detect_frame(frame)
            
            for label in results["labels"]:
                label_name = detector.model.config.id2label[label.item()]
                if label_name in target_objects:
                    object_counts[label_name] += 1
        
        frame_count += 1
    
    cap.release()
    
    print("Object tellingen:")
    for obj, count in object_counts.items():
        print(f"  {obj}: {count}")
    
    return object_counts
```

## 6. Performance tips

### Optimalisatie strategieën

1. **Frame skipping**: Process niet elke frame
```python
# Process elke 3e frame
if frame_count % 3 == 0:
    detections = detect_objects(frame)
```

2. **Resize frames**: Kleinere input voor snellere processing
```python
# Resize naar 640x640 voor snellere detection
resized_frame = cv2.resize(frame, (640, 640))
```

3. **GPU acceleration**: Gebruik CUDA als beschikbaar
```python
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)
```

4. **Batch processing**: Process meerdere frames tegelijk
```python
# Voor offline video processing
batch_frames = [frame1, frame2, frame3]
results = processor(images=batch_frames, return_tensors="pt")
```

## 7. Alternatieve implementaties

Voor verschillende use cases en voorkeuren zijn er meerdere implementaties beschikbaar:

### Ultralytics YOLO (Aanbevolen voor beginners)
```python
from ultralytics import YOLO

# Simpel en snel
model = YOLO("yolov8n.pt")  # nano model voor snelheid
results = model("chair_video.mp4")

# Automatische visualisatie
for result in results:
    result.show()
```

**Voordelen**: Zeer eenvoudig, goede documentatie, built-in tracking
**Nadelen**: Minder flexibiliteit voor custom experimenten

### OpenCV DNN (Minimale dependencies)
```python
import cv2

# Laad pre-trained YOLO model
net = cv2.dnn.readNet("yolov4.weights", "yolov4.cfg")

# Inference
blob = cv2.dnn.blobFromImage(image, 1/255.0, (416, 416))
net.setInput(blob)
outputs = net.forward()
```

**Voordelen**: Geen ML framework needed, zeer lichtgewicht
**Nadelen**: Meer boilerplate code, minder model opties

### TensorFlow Hub
```python
import tensorflow_hub as hub

# Laad model van TF Hub
model = hub.load("https://tfhub.dev/tensorflow/ssd_mobilenet_v2/2")
detections = model(image_tensor)
```

**Voordelen**: Productie-klaar, goede mobile ondersteuning
**Nadelen**: Minder cutting-edge modellen dan HuggingFace

Zie `alternatives.py` voor complete implementaties van alle benaderingen.

## Volgende stappen

- **Experimenteer** met `alternatives.py` om verschillende frameworks te vergelijken
- **Kies** de beste benadering voor jouw project requirements
- **Probeer** custom object detection training
- **Integreer** met tracking algoritmes (DeepSORT, ByteTrack)
- **Bouw** een web interface voor video upload
- **Optimaliseer** voor jouw specifieke hardware (CPU/GPU/Edge devices)

---

*Tip: Begin met Ultralytics YOLO voor snelle resultaten, ga naar PyTorch + Transformers voor research en experimenten.*