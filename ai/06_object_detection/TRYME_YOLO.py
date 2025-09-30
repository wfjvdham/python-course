#!/usr/bin/env python3
"""
YOLO Object Detection - Better for Chairs
=========================================

Alternative script using YOLOv5 which is often better at detecting furniture.
"""

import cv2
import torch
import numpy as np
from pathlib import Path
import argparse

# Try to import YOLOv5
try:
    import yolov5
    YOLO_AVAILABLE = True
except ImportError:
    YOLO_AVAILABLE = False
    print("⚠️  YOLOv5 not available. Install with: pip install yolov5")

def detect_with_yolo(video_path, output_path, confidence=0.5):
    """Use YOLOv5 for object detection"""
    if not YOLO_AVAILABLE:
        print("❌ YOLOv5 not installed")
        return
    
    # Load YOLOv5 model
    print("🔄 Loading YOLOv5 model...")
    model = yolov5.load('yolov5s.pt')
    model.conf = confidence  # confidence threshold
    print("✅ YOLOv5 model loaded")
    
    # Open video
    cap = cv2.VideoCapture(str(video_path))
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    
    print(f"📊 Video: {width}x{height}, {fps} FPS, {total_frames} frames")
    
    # Output writer
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    writer = cv2.VideoWriter(str(output_path), fourcc, fps, (width, height))
    
    frame_count = 0
    detection_stats = {}
    
    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            
            # Progress
            if frame_count % 30 == 0:
                progress = (frame_count / total_frames) * 100
                print(f"🔄 Progress: {progress:.1f}%")
            
            # YOLO detection every 3rd frame
            if frame_count % 3 == 0:
                results = model(frame)
                
                # Process results
                for *box, conf, cls in results.xyxy[0].cpu().numpy():
                    if conf > confidence:
                        x1, y1, x2, y2 = map(int, box)
                        label = model.names[int(cls)]
                        
                        # Statistics
                        if label not in detection_stats:
                            detection_stats[label] = {"count": 0, "confidences": []}
                        detection_stats[label]["count"] += 1
                        detection_stats[label]["confidences"].append(conf)
                        
                        # Draw on frame
                        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                        cv2.putText(frame, f"{label}: {conf:.2f}", 
                                   (x1, max(30, y1 - 10)), 
                                   cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
            
            writer.write(frame)
            frame_count += 1
            
    finally:
        cap.release()
        writer.release()
        cv2.destroyAllWindows()
    
    # Print statistics
    print(f"\n📈 YOLO Detection Statistics:")
    for label, stats in sorted(detection_stats.items(), key=lambda x: x[1]["count"], reverse=True):
        count = stats["count"]
        confidences = stats["confidences"]
        if confidences:
            avg_conf = sum(confidences) / len(confidences)
            min_conf = min(confidences)
            max_conf = max(confidences)
            print(f"  {label}: {count} detections (avg: {avg_conf:.3f}, min: {min_conf:.3f}, max: {max_conf:.3f})")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="YOLO Object Detection")
    parser.add_argument("--input", required=True, help="Input video path")
    parser.add_argument("--output", required=True, help="Output video path")
    parser.add_argument("--confidence", type=float, default=0.5, help="Confidence threshold")
    
    args = parser.parse_args()
    
    detect_with_yolo(args.input, args.output, args.confidence)