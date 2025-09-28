#!/usr/bin/env python3
"""
Alternative Object Detection Implementations
============================================

This file shows different approaches to object detection without PyTorch,
giving students lighter alternatives for different use cases.
"""

import cv2
import numpy as np
from pathlib import Path
import time

class OpenCVObjectDetector:
    """Lightweight object detection using OpenCV DNN module"""
    
    def __init__(self):
        """Initialize with pre-trained COCO model"""
        self.net = None
        self.classes = []
        self.colors = []
        self.confidence_threshold = 0.5
        self.nms_threshold = 0.4
        
        # Try to load a pre-trained model
        self.load_yolo_model()
    
    def load_yolo_model(self):
        """Load YOLOv4 model from OpenCV"""
        try:
            # Note: These files need to be downloaded separately
            weights_path = "yolov4.weights"
            config_path = "yolov4.cfg" 
            names_path = "coco.names"
            
            # Check if files exist
            if not all(Path(p).exists() for p in [weights_path, config_path, names_path]):
                print("⚠️  YOLO model files not found. Use download_yolo_model() first.")
                return False
            
            # Load network
            self.net = cv2.dnn.readNet(weights_path, config_path)
            
            # Load class names
            with open(names_path, 'r') as f:
                self.classes = [line.strip() for line in f.readlines()]
            
            # Generate colors for each class
            self.colors = np.random.uniform(0, 255, size=(len(self.classes), 3))
            
            print(f"✅ OpenCV YOLO model loaded with {len(self.classes)} classes")
            return True
            
        except Exception as e:
            print(f"❌ Error loading YOLO model: {e}")
            return False
    
    def download_yolo_model(self):
        """Download YOLO model files"""
        import urllib.request
        
        files = {
            "yolov4.weights": "https://github.com/AlexeyAB/darknet/releases/download/darknet_yolo_v3_optimal/yolov4.weights",
            "yolov4.cfg": "https://raw.githubusercontent.com/AlexeyAB/darknet/master/cfg/yolov4.cfg",
            "coco.names": "https://raw.githubusercontent.com/AlexeyAB/darknet/master/data/coco.names"
        }
        
        print("📥 Downloading YOLO model files...")
        for filename, url in files.items():
            if not Path(filename).exists():
                print(f"   Downloading {filename}...")
                urllib.request.urlretrieve(url, filename)
        
        print("✅ YOLO model files downloaded")
        self.load_yolo_model()
    
    def detect_objects(self, image):
        """Detect objects in image using OpenCV DNN"""
        if self.net is None:
            return []
        
        height, width = image.shape[:2]
        
        # Create blob from image
        blob = cv2.dnn.blobFromImage(image, 1/255.0, (416, 416), swapRB=True, crop=False)
        
        # Set input to network
        self.net.setInput(blob)
        
        # Run forward pass
        layer_outputs = self.net.forward(self.net.getUnconnectedOutLayersNames())
        
        # Process outputs
        boxes = []
        confidences = []
        class_ids = []
        
        for output in layer_outputs:
            for detection in output:
                scores = detection[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]
                
                if confidence > self.confidence_threshold:
                    # Scale back to original image
                    center_x = int(detection[0] * width)
                    center_y = int(detection[1] * height)
                    w = int(detection[2] * width)
                    h = int(detection[3] * height)
                    
                    x = int(center_x - w/2)
                    y = int(center_y - h/2)
                    
                    boxes.append([x, y, w, h])
                    confidences.append(float(confidence))
                    class_ids.append(class_id)
        
        # Apply non-maximum suppression
        indices = cv2.dnn.NMSBoxes(boxes, confidences, self.confidence_threshold, self.nms_threshold)
        
        detections = []
        if len(indices) > 0:
            for i in indices.flatten():
                x, y, w, h = boxes[i]
                detections.append({
                    "label": self.classes[class_ids[i]],
                    "confidence": confidences[i],
                    "box": [x, y, x + w, y + h]
                })
        
        return detections

class UltralyticsDetector:
    """Simple YOLO detection using Ultralytics"""
    
    def __init__(self, model_name="yolov8n.pt"):
        """Initialize with Ultralytics YOLO model"""
        try:
            from ultralytics import YOLO
            self.model = YOLO(model_name)
            print(f"✅ Ultralytics YOLO model loaded: {model_name}")
        except ImportError:
            print("❌ Ultralytics not installed. Run: pip install ultralytics")
            self.model = None
    
    def detect_objects(self, image):
        """Detect objects using Ultralytics YOLO"""
        if self.model is None:
            return []
        
        # Run inference
        results = self.model(image)
        
        detections = []
        for result in results:
            boxes = result.boxes
            if boxes is not None:
                for box in boxes:
                    # Get box coordinates
                    x1, y1, x2, y2 = box.xyxy[0].cpu().numpy()
                    
                    # Get confidence and class
                    confidence = box.conf[0].cpu().numpy()
                    class_id = int(box.cls[0].cpu().numpy())
                    
                    detections.append({
                        "label": self.model.names[class_id],
                        "confidence": float(confidence),
                        "box": [int(x1), int(y1), int(x2), int(y2)]
                    })
        
        return detections

class TensorFlowDetector:
    """TensorFlow object detection implementation"""
    
    def __init__(self):
        """Initialize TensorFlow detector"""
        try:
            import tensorflow as tf
            import tensorflow_hub as hub
            
            # Load model from TensorFlow Hub
            model_url = "https://tfhub.dev/tensorflow/ssd_mobilenet_v2/2"
            self.model = hub.load(model_url)
            
            # COCO class names
            self.class_names = [
                "person", "bicycle", "car", "motorcycle", "airplane", "bus", "train", "truck",
                "boat", "traffic light", "fire hydrant", "stop sign", "parking meter", "bench",
                "bird", "cat", "dog", "horse", "sheep", "cow", "elephant", "bear", "zebra", 
                "giraffe", "backpack", "umbrella", "handbag", "tie", "suitcase", "frisbee",
                "skis", "snowboard", "sports ball", "kite", "baseball bat", "baseball glove",
                "skateboard", "surfboard", "tennis racket", "bottle", "wine glass", "cup",
                "fork", "knife", "spoon", "bowl", "banana", "apple", "sandwich", "orange",
                "broccoli", "carrot", "hot dog", "pizza", "donut", "cake", "chair", "couch",
                "potted plant", "bed", "dining table", "toilet", "tv", "laptop", "mouse",
                "remote", "keyboard", "cell phone", "microwave", "oven", "toaster", "sink",
                "refrigerator", "book", "clock", "vase", "scissors", "teddy bear", "hair drier", "toothbrush"
            ]
            
            print("✅ TensorFlow model loaded")
            
        except ImportError:
            print("❌ TensorFlow not installed. Run: pip install tensorflow tensorflow-hub")
            self.model = None
    
    def detect_objects(self, image):
        """Detect objects using TensorFlow"""
        if self.model is None:
            return []
        
        import tensorflow as tf
        
        # Prepare image
        input_tensor = tf.convert_to_tensor(image)
        input_tensor = input_tensor[tf.newaxis, ...]
        
        # Run inference
        detections = self.model(input_tensor)
        
        # Process results
        detection_boxes = detections['detection_boxes'][0].numpy()
        detection_classes = detections['detection_classes'][0].numpy().astype(int)
        detection_scores = detections['detection_scores'][0].numpy()
        
        height, width = image.shape[:2]
        results = []
        
        for i in range(len(detection_scores)):
            if detection_scores[i] > 0.5:  # Confidence threshold
                # Convert normalized coordinates to pixel coordinates
                y1, x1, y2, x2 = detection_boxes[i]
                x1, y1, x2, y2 = int(x1 * width), int(y1 * height), int(x2 * width), int(y2 * height)
                
                class_id = detection_classes[i]
                if class_id < len(self.class_names):
                    results.append({
                        "label": self.class_names[class_id],
                        "confidence": float(detection_scores[i]),
                        "box": [x1, y1, x2, y2]
                    })
        
        return results

def benchmark_detectors(image_path):
    """Compare performance of different detectors"""
    print("🏁 Benchmarking different object detection approaches...")
    
    # Load test image
    image = cv2.imread(str(image_path))
    if image is None:
        print(f"❌ Cannot load image: {image_path}")
        return
    
    detectors = {
        "OpenCV DNN": OpenCVObjectDetector(),
        "Ultralytics YOLO": UltralyticsDetector(),
        "TensorFlow Hub": TensorFlowDetector()
    }
    
    results = {}
    
    for name, detector in detectors.items():
        print(f"\n🔄 Testing {name}...")
        
        try:
            start_time = time.time()
            detections = detector.detect_objects(image)
            inference_time = time.time() - start_time
            
            results[name] = {
                "inference_time": inference_time,
                "num_detections": len(detections),
                "detections": detections
            }
            
            print(f"   ⏱️  Time: {inference_time:.3f}s")
            print(f"   🎯 Detections: {len(detections)}")
            
            # Show top 3 detections
            sorted_detections = sorted(detections, key=lambda x: x['confidence'], reverse=True)
            for i, det in enumerate(sorted_detections[:3]):
                print(f"      {i+1}. {det['label']}: {det['confidence']:.3f}")
        
        except Exception as e:
            print(f"   ❌ Error: {e}")
            results[name] = {"error": str(e)}
    
    # Summary
    print(f"\n📊 Benchmark Summary:")
    print(f"{'Method':<20} {'Time (s)':<10} {'Detections':<12} {'Status'}")
    print("-" * 50)
    
    for name, result in results.items():
        if "error" in result:
            print(f"{name:<20} {'N/A':<10} {'N/A':<12} ❌ {result['error'][:20]}...")
        else:
            time_str = f"{result['inference_time']:.3f}"
            count_str = str(result['num_detections'])
            print(f"{name:<20} {time_str:<10} {count_str:<12} ✅")

def main():
    """Demo the different detection approaches"""
    print("🔍 Alternative Object Detection Methods Demo")
    print("=" * 50)
    
    # Create a simple test image if none exists
    test_image = "chair_test.jpg"
    
    if not Path(test_image).exists():
        print(f"⚠️  Test image not found: {test_image}")
        print("   Create one with: python create_chair_video.py --image")
        return
    
    # Run benchmark
    benchmark_detectors(test_image)
    
    print("\n💡 Recommendations:")
    print("• OpenCV DNN: Lightweight, no ML framework needed")
    print("• Ultralytics: Easiest setup, great for beginners") 
    print("• TensorFlow: Good for production, ecosystem support")
    print("• PyTorch + Transformers: Best for research, latest models")

if __name__ == "__main__":
    main()