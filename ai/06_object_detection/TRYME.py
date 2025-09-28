#!/usr/bin/env python3
"""
Object Detection Video Example
==============================

Dit script demonstreert object detection op video's met Hugging Face Transformers.
Het kan werken met webcam, video bestanden en afbeeldingen.

Gebruik:
    python TRYME.py --input webcam
    python TRYME.py --input video.mp4 --output result.mp4
    python TRYME.py --input image.jpg --save-image
"""

import argparse
import cv2
import torch
import numpy as np
from PIL import Image, ImageDraw
import matplotlib.pyplot as plt
from pathlib import Path
import time

# Probeer transformers te importeren
try:
    from transformers import DetrImageProcessor, DetrForObjectDetection
    TRANSFORMERS_AVAILABLE = True
except ImportError:
    TRANSFORMERS_AVAILABLE = False
    print("⚠️  Transformers niet geïnstalleerd. Installeer met: pip install transformers torch")

class SimpleObjectDetector:
    """Eenvoudige object detector met DETR model"""
    
    def __init__(self, model_name="facebook/detr-resnet-50", confidence_threshold=0.8):
        if not TRANSFORMERS_AVAILABLE:
            raise ImportError("Transformers library is required")
        
        print(f"🔄 Model laden: {model_name}")
        self.processor = DetrImageProcessor.from_pretrained(model_name)
        self.model = DetrForObjectDetection.from_pretrained(model_name)
        self.confidence_threshold = confidence_threshold
        
        # GPU ondersteuning
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model.to(self.device)
        print(f"✅ Model geladen op: {self.device}")
        
    def detect_objects(self, image):
        """Detecteer objecten in een PIL Image"""
        # Preprocessing
        inputs = self.processor(images=image, return_tensors="pt")
        inputs = {k: v.to(self.device) for k, v in inputs.items()}
        
        # Inference
        with torch.no_grad():
            outputs = self.model(**inputs)
        
        # Postprocessing
        target_sizes = torch.tensor([image.size[::-1]]).to(self.device)
        results = self.processor.post_process_object_detection(
            outputs, target_sizes=target_sizes, threshold=self.confidence_threshold
        )[0]
        
        # Resultaten formatteren
        detections = []
        for score, label, box in zip(results["scores"], results["labels"], results["boxes"]):
            detections.append({
                "label": self.model.config.id2label[label.item()],
                "confidence": score.item(),
                "box": box.cpu().numpy().astype(int)  # [x_min, y_min, x_max, y_max]
            })
        
        return detections

def draw_detections_pil(image, detections):
    """Teken detecties op PIL image"""
    draw = ImageDraw.Draw(image)
    
    for detection in detections:
        box = detection["box"]
        label = detection["label"]
        confidence = detection["confidence"]
        
        # Bounding box
        draw.rectangle(box.tolist(), outline="red", width=3)
        
        # Label
        text = f"{label}: {confidence:.2f}"
        draw.text((box[0], max(0, box[1] - 20)), text, fill="red")
    
    return image

def draw_detections_cv2(frame, detections):
    """Teken detecties op OpenCV frame"""
    for detection in detections:
        box = detection["box"]
        label = detection["label"]
        confidence = detection["confidence"]
        
        # Bounding box
        cv2.rectangle(frame, (box[0], box[1]), (box[2], box[3]), (0, 255, 0), 2)
        
        # Label
        text = f"{label}: {confidence:.2f}"
        cv2.putText(frame, text, (box[0], max(30, box[1] - 10)), 
                   cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
    
    return frame

def process_image(image_path, detector, save_result=False):
    """Process een enkele afbeelding"""
    print(f"🖼️  Processing afbeelding: {image_path}")
    
    # Afbeelding laden
    image = Image.open(image_path).convert("RGB")
    
    # Object detection
    start_time = time.time()
    detections = detector.detect_objects(image)
    detection_time = time.time() - start_time
    
    # Resultaten printen
    print(f"⏱️  Detection tijd: {detection_time:.2f}s")
    print(f"🎯 Gevonden objecten: {len(detections)}")
    
    for i, detection in enumerate(detections):
        print(f"  {i+1}. {detection['label']}: {detection['confidence']:.3f}")
    
    # Visualisatie
    result_image = draw_detections_pil(image.copy(), detections)
    
    if save_result:
        output_path = Path(image_path).stem + "_detected.jpg"
        result_image.save(output_path)
        print(f"💾 Resultaat opgeslagen: {output_path}")
    
    # Tonen
    plt.figure(figsize=(12, 8))
    plt.imshow(result_image)
    plt.axis('off')
    plt.title(f"Object Detection - {len(detections)} objecten gevonden")
    plt.tight_layout()
    plt.show()
    
    return detections

def process_webcam(detector):
    """Process webcam feed real-time"""
    print("📹 Webcam openen... (druk 'q' om te stoppen)")
    
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("❌ Kan webcam niet openen")
        return
    
    frame_count = 0
    fps_counter = 0
    start_time = time.time()
    
    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            
            # Process elke 5e frame voor betere performance
            if frame_count % 5 == 0:
                # OpenCV naar PIL
                rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                pil_image = Image.fromarray(rgb_frame)
                
                # Object detection
                detections = detector.detect_objects(pil_image)
                
                # Tekenen op frame
                frame = draw_detections_cv2(frame, detections)
                
                # FPS berekenen
                fps_counter += 1
                if fps_counter % 10 == 0:
                    elapsed = time.time() - start_time
                    fps = fps_counter / elapsed
                    print(f"🚀 Processing FPS: {fps:.1f}")
            
            # Info op frame
            cv2.putText(frame, f"Frame: {frame_count}", (10, 30), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
            
            # Tonen
            cv2.imshow('Object Detection - Druk Q om te stoppen', frame)
            
            # Stoppen met 'q'
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            
            frame_count += 1
            
    finally:
        cap.release()
        cv2.destroyAllWindows()

def process_video(video_path, detector, output_path=None):
    """Process video bestand"""
    print(f"🎬 Processing video: {video_path}")
    
    cap = cv2.VideoCapture(str(video_path))
    
    if not cap.isOpened():
        print(f"❌ Kan video niet openen: {video_path}")
        return
    
    # Video properties
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    
    print(f"📊 Video info: {width}x{height}, {fps} FPS, {total_frames} frames")
    
    # Output video writer
    writer = None
    if output_path:
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        writer = cv2.VideoWriter(str(output_path), fourcc, fps, (width, height))
        print(f"💾 Output wordt opgeslagen naar: {output_path}")
    
    frame_count = 0
    detection_stats = {}
    
    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            
            # Progress
            progress = (frame_count / total_frames) * 100
            if frame_count % 30 == 0:  # Elke seconde bij 30fps
                print(f"🔄 Progress: {progress:.1f}%")
            
            # Process elke 3e frame
            if frame_count % 3 == 0:
                # OpenCV naar PIL
                rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                pil_image = Image.fromarray(rgb_frame)
                
                # Object detection
                detections = detector.detect_objects(pil_image)
                
                # Statistieken bijhouden
                for detection in detections:
                    label = detection["label"]
                    detection_stats[label] = detection_stats.get(label, 0) + 1
                
                # Tekenen op frame
                frame = draw_detections_cv2(frame, detections)
            
            # Opslaan
            if writer:
                writer.write(frame)
            
            # Live preview (optioneel)
            cv2.imshow('Processing Video - Druk Q om te stoppen', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            
            frame_count += 1
            
    finally:
        cap.release()
        if writer:
            writer.release()
        cv2.destroyAllWindows()
    
    # Statistieken printen
    print(f"\n📈 Detectie statistieken:")
    for label, count in sorted(detection_stats.items(), key=lambda x: x[1], reverse=True):
        print(f"  {label}: {count} detecties")

def create_sample_video_with_chair():
    """Maak een eenvoudige test video met een stoel (placeholder)"""
    print("🎨 Sample video maken...")
    
    # Simpel voorbeeld: tekst overlay op een gekleurde achtergrond
    width, height = 640, 480
    fps = 30
    duration = 10  # seconden
    
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter('sample_chair_video.mp4', fourcc, fps, (width, height))
    
    for frame_num in range(fps * duration):
        # Maak een frame
        frame = np.random.randint(50, 100, (height, width, 3), dtype=np.uint8)
        
        # Voeg tekst toe
        cv2.putText(frame, "Sample Video - Place Real Chair Video Here", 
                   (50, height//2), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
        cv2.putText(frame, f"Frame: {frame_num}", 
                   (50, height//2 + 50), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (200, 200, 200), 2)
        
        out.write(frame)
    
    out.release()
    print("✅ Sample video gemaakt: sample_chair_video.mp4")

def main():
    parser = argparse.ArgumentParser(description="Object Detection Demo")
    parser.add_argument("--input", required=True, 
                       help="Input: 'webcam', image path, of video path")
    parser.add_argument("--output", 
                       help="Output video pad (alleen voor video input)")
    parser.add_argument("--confidence", type=float, default=0.8,
                       help="Minimum confidence threshold (default: 0.8)")
    parser.add_argument("--save-image", action="store_true",
                       help="Sla resultaat afbeelding op")
    parser.add_argument("--create-sample", action="store_true",
                       help="Maak sample video")
    
    args = parser.parse_args()
    
    # Sample video maken
    if args.create_sample:
        create_sample_video_with_chair()
        return
    
    # Check of transformers beschikbaar is
    if not TRANSFORMERS_AVAILABLE:
        print("❌ Installeer eerst de benodigde packages:")
        print("   pip install transformers torch torchvision opencv-python pillow matplotlib")
        return
    
    # Detector initialiseren
    try:
        detector = SimpleObjectDetector(confidence_threshold=args.confidence)
    except Exception as e:
        print(f"❌ Fout bij initialiseren detector: {e}")
        return
    
    # Input verwerken
    if args.input.lower() == "webcam":
        process_webcam(detector)
    elif Path(args.input).suffix.lower() in ['.jpg', '.jpeg', '.png', '.bmp']:
        process_image(args.input, detector, args.save_image)
    elif Path(args.input).suffix.lower() in ['.mp4', '.avi', '.mov', '.mkv']:
        process_video(args.input, detector, args.output)
    else:
        print(f"❌ Onbekend input formaat: {args.input}")
        print("   Ondersteunde formaten: webcam, jpg/png (afbeeldingen), mp4/avi (video's)")

if __name__ == "__main__":
    print("🤖 Object Detection Demo")
    print("=" * 40)
    
    # Controleer of er argumenten zijn gegeven
    import sys
    if len(sys.argv) == 1:
        print("📚 Geen argumenten gegeven. Hier zijn enkele voorbeelden:")
        print()
        print("Webcam gebruiken:")
        print("  python TRYME.py --input webcam")
        print()
        print("Afbeelding verwerken:")
        print("  python TRYME.py --input photo.jpg --save-image")
        print()
        print("Video verwerken:")
        print("  python TRYME.py --input video.mp4 --output result.mp4")
        print()
        print("Sample video maken:")
        print("  python TRYME.py --create-sample")
        print()
        print("Voor meer opties: python TRYME.py --help")
    else:
        main()