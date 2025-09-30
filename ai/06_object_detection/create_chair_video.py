#!/usr/bin/env python3
"""
Simple Chair Video Creator
==========================

Creates a basic MP4 video with a simple chair drawing for testing object detection.
This script uses only PIL and basic graphics to create a test video.

Usage:
    python create_chair_video.py
"""

import os
from PIL import Image, ImageDraw, ImageFont
import subprocess
import sys

def create_chair_frame(frame_number, total_frames, width=640, height=480):
    """Create a single frame with a simple, recognizable chair"""
    
    # Create image with simple background
    img = Image.new('RGB', (width, height), color=(240, 240, 240))  # Light gray background
    draw = ImageDraw.Draw(img)
    
    # Simple floor
    floor_y = height - 60
    draw.rectangle([0, floor_y, width, height], fill=(200, 200, 200))  # Gray floor
    
    # Simple chair animation - just slight left-right movement
    animation_progress = frame_number / total_frames
    chair_x = int(width * 0.4 + 40 * (0.5 - 0.5 * abs(2 * animation_progress - 1)))
    chair_y = floor_y - 100
    
    # Chair colors - simple and clear
    wood_brown = (139, 69, 19)
    darker_brown = (101, 67, 33)
    
    # SIMPLE CHAIR DESIGN - like a dining chair
    
    # 1. Chair legs (4 simple rectangles)
    leg_width = 6
    leg_height = 60
    
    # Front left leg
    draw.rectangle([
        chair_x + 15, chair_y + 40,
        chair_x + 15 + leg_width, chair_y + 40 + leg_height
    ], fill=wood_brown, outline=darker_brown)
    
    # Front right leg  
    draw.rectangle([
        chair_x + 65, chair_y + 40,
        chair_x + 65 + leg_width, chair_y + 40 + leg_height
    ], fill=wood_brown, outline=darker_brown)
    
    # Back left leg
    draw.rectangle([
        chair_x + 15, chair_y + 5,
        chair_x + 15 + leg_width, chair_y + 45
    ], fill=wood_brown, outline=darker_brown)
    
    # Back right leg
    draw.rectangle([
        chair_x + 65, chair_y + 5,
        chair_x + 65 + leg_width, chair_y + 45
    ], fill=wood_brown, outline=darker_brown)
    
    # 2. Seat (simple rectangle with rounded appearance)
    draw.rectangle([
        chair_x + 10, chair_y + 35,
        chair_x + 76, chair_y + 50
    ], fill=wood_brown, outline=darker_brown, width=2)
    
    # 3. Backrest (simple tall rectangle)
    draw.rectangle([
        chair_x + 10, chair_y,
        chair_x + 76, chair_y + 40
    ], fill=wood_brown, outline=darker_brown, width=2)
    
    # Add simple shadow
    draw.ellipse([
        chair_x + 5, chair_y + 95,
        chair_x + 85, chair_y + 105
    ], fill=(180, 180, 180))
    
    # Add frame counter
    try:
        font = ImageFont.load_default()
    except:
        font = None
    
    draw.text((10, 10), f"Frame: {frame_number}/{total_frames}", fill=(100, 100, 100), font=font)
    draw.text((10, height - 30), "Simple Chair Test", fill=(100, 100, 100), font=font)
    
    return img
    
    # Add some subtle room elements to make it more realistic
    # Wall
    draw.rectangle([0, 0, width, floor_y], fill=(245, 245, 220))  # Light beige wall
    
    # Add subtle wall texture
    for i in range(0, width, 40):
        draw.line([i, 0, i, floor_y], fill=(240, 240, 215), width=1)
    
    # Window or light source (subtle)
    window_x = width - 120
    draw.rectangle([window_x, 20, window_x + 80, 120], fill=(255, 255, 240), outline=(200, 200, 180), width=2)
    
    # Window light reflection on floor
    light_points = [
        (chair_x + chair_width + 20, floor_y),
        (chair_x + chair_width + 60, floor_y),
        (chair_x + chair_width + 50, floor_y + 20),
        (chair_x + chair_width + 10, floor_y + 20)
    ]
    draw.polygon(light_points, fill=(120, 85, 45))  # Lighter floor area
    
    # Add frame counter and info text
    try:
        # Try to use default font
        font = ImageFont.load_default()
    except:
        font = None
    
    text_color = (100, 100, 100)  # Gray text
    draw.text((10, 10), f"Frame: {frame_number}/{total_frames}", fill=text_color, font=font)
    draw.text((10, height - 30), "Realistic Chair for Object Detection", fill=text_color, font=font)
    
    return img

def create_chair_video(output_filename="chair_video_simple.mp4", duration=10, fps=25):
    """Create a video with animated chair"""
    
    # Get the directory where this script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    total_frames = duration * fps
    temp_dir = os.path.join(script_dir, "temp_frames")
    output_path = os.path.join(script_dir, output_filename)
    
    print(f"🎬 Creating chair video: {output_filename}")
    print(f"   Duration: {duration}s, FPS: {fps}, Total frames: {total_frames}")
    
    # Create temp directory for frames
    if not os.path.exists(temp_dir):
        os.makedirs(temp_dir)
    
    # Generate all frames
    print("🎨 Generating frames...")
    for frame_num in range(total_frames):
        if frame_num % (total_frames // 10) == 0:  # Progress updates
            progress = (frame_num / total_frames) * 100
            print(f"   Progress: {progress:.0f}%")
        
        frame = create_chair_frame(frame_num, total_frames)
        frame_path = os.path.join(temp_dir, f"frame_{frame_num:06d}.png")
        frame.save(frame_path)
    
    # Create video using ffmpeg
    print("🎞️  Combining frames into video...")
    
    # Check if ffmpeg is available
    try:
        subprocess.run(['ffmpeg', '-version'], capture_output=True, check=True)
        ffmpeg_available = True
    except (subprocess.CalledProcessError, FileNotFoundError):
        ffmpeg_available = False
    
    if ffmpeg_available:
        # Use ffmpeg to create video
        cmd = [
            'ffmpeg', '-y',  # -y to overwrite
            '-framerate', str(fps),
            '-i', f'{temp_dir}/frame_%06d.png',
            '-c:v', 'libx264',
            '-pix_fmt', 'yuv420p',
            '-crf', '23',
            output_path
        ]
        
        try:
            result = subprocess.run(cmd, capture_output=True, text=True)
            if result.returncode == 0:
                print(f"✅ Video created successfully: {output_path}")
            else:
                print(f"❌ FFmpeg error: {result.stderr}")
                return False
        except Exception as e:
            print(f"❌ Error running ffmpeg: {e}")
            return False
    else:
        print("⚠️  FFmpeg not found. Alternative: use online converter or install ffmpeg")
        print("   Frames are available in:", temp_dir)
        print("   You can manually convert them to video using:")
        print(f"   ffmpeg -framerate {fps} -i {temp_dir}/frame_%06d.png -c:v libx264 {output_path}")
        return False
    
    # Cleanup temp files
    print("🧹 Cleaning up temporary files...")
    import shutil
    shutil.rmtree(temp_dir)
    
    return True

def create_chair_image(filename="chair_test.jpg"):
    """Create a single test image with a chair"""
    # Get the directory where this script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(script_dir, filename)
    
    print(f"📸 Creating test image: {output_path}")
    
    # Use the most photorealistic version for better detection
    frame = create_photorealistic_chair_image()
    frame.save(output_path)
    
    print(f"✅ Test image created: {output_path}")
    return True

def create_enhanced_chair_image(width=640, height=480):
    """Create an enhanced static chair image with better detection features"""
    
    # Create image with simple background
    img = Image.new('RGB', (width, height), color=(245, 245, 245))  # Light background
    draw = ImageDraw.Draw(img)
    
    # Add a simple room context - floor and wall
    floor_y = height - 60
    draw.rectangle([0, floor_y, width, height], fill=(210, 180, 140))  # Wooden floor
    
    # Add simple wall baseboard
    draw.rectangle([0, floor_y - 10, width, floor_y], fill=(180, 180, 180))
    
    # Position chair in center for optimal detection
    chair_x = width // 2 - 40  # Centered
    chair_y = floor_y - 100
    
    # Chair colors - more realistic
    wood_brown = (139, 69, 19)
    darker_brown = (101, 67, 33)
    seat_color = (160, 82, 45)  # Slightly lighter for seat
    
    # Draw chair with enhanced details for better recognition
    
    # 1. Chair legs with slight 3D effect
    leg_width = 8
    leg_height = 60
    
    # Front left leg
    draw.rectangle([
        chair_x + 15, chair_y + 40,
        chair_x + 15 + leg_width, chair_y + 40 + leg_height
    ], fill=wood_brown, outline=darker_brown, width=1)
    
    # Front right leg  
    draw.rectangle([
        chair_x + 65, chair_y + 40,
        chair_x + 65 + leg_width, chair_y + 40 + leg_height
    ], fill=wood_brown, outline=darker_brown, width=1)
    
    # Back left leg
    draw.rectangle([
        chair_x + 15, chair_y + 5,
        chair_x + 15 + leg_width, chair_y + 45
    ], fill=wood_brown, outline=darker_brown, width=1)
    
    # Back right leg
    draw.rectangle([
        chair_x + 65, chair_y + 5,
        chair_x + 65 + leg_width, chair_y + 45
    ], fill=wood_brown, outline=darker_brown, width=1)
    
    # 2. Seat with slight perspective and padding
    draw.rectangle([
        chair_x + 10, chair_y + 35,
        chair_x + 76, chair_y + 50
    ], fill=seat_color, outline=darker_brown, width=2)
    
    # Add seat edge detail
    draw.rectangle([
        chair_x + 12, chair_y + 37,
        chair_x + 74, chair_y + 48
    ], fill=wood_brown, outline=None)
    
    # 3. Backrest with more defined shape
    draw.rectangle([
        chair_x + 12, chair_y,
        chair_x + 74, chair_y + 40
    ], fill=wood_brown, outline=darker_brown, width=2)
    
    # Add backrest detail/slats
    for i in range(3):
        slat_x = chair_x + 20 + i * 15
        draw.rectangle([
            slat_x, chair_y + 5,
            slat_x + 8, chair_y + 35
        ], fill=seat_color, outline=darker_brown, width=1)
    
    # 4. Add chair shadow on floor for realism
    shadow_color = (190, 160, 120)
    draw.ellipse([
        chair_x + 5, chair_y + 95,
        chair_x + 85, chair_y + 110
    ], fill=shadow_color)
    
    # 5. Add some contextual elements that help with detection
    # Small table leg visible in corner
    draw.rectangle([
        width - 30, floor_y - 40,
        width - 25, floor_y
    ], fill=(101, 67, 33))
    
    # Part of a wall or furniture edge
    draw.rectangle([
        0, 0,
        5, height // 2
    ], fill=(200, 200, 200))
    
    return img


def create_photorealistic_chair_image():
    """Create a highly detailed, photorealistic chair image"""
    img = Image.new('RGB', (400, 400), 'white')
    draw = ImageDraw.Draw(img)
    
    # Room background - gradient wall
    for y in range(0, 300):
        color_val = int(250 - (y * 20 / 300))
        draw.line([(0, y), (400, y)], fill=(color_val, color_val-5, color_val-10))
    
    # Wooden floor with planks
    floor_base = (210, 180, 140)
    for y in range(300, 400, 20):
        plank_color = (floor_base[0] + (y % 40 - 20), 
                      floor_base[1] + (y % 30 - 15), 
                      floor_base[2] + (y % 25 - 12))
        draw.rectangle([(0, y), (400, y+18)], fill=plank_color)
        draw.line([(0, y+18), (400, y+18)], fill=(150, 120, 90))  # Plank lines
    
    # Chair - detailed wooden dining chair
    wood_main = (101, 67, 33)
    wood_light = (139, 90, 43)
    wood_dark = (80, 53, 26)
    
    # Chair seat - rounded corners and depth
    seat_points = [(140, 190), (260, 190), (270, 210), (130, 210)]
    draw.polygon(seat_points, fill=wood_main)
    # Seat edge highlighting
    draw.polygon([(140, 190), (260, 190), (260, 195), (140, 195)], fill=wood_light)
    draw.polygon([(130, 210), (270, 210), (270, 215), (130, 215)], fill=wood_dark)
    
    # Backrest - traditional ladder-back style
    # Main backrest frame
    draw.rectangle([(145, 100), (155, 195)], fill=wood_main)  # Left post
    draw.rectangle([(245, 100), (255, 195)], fill=wood_main)  # Right post
    draw.rectangle([(155, 100), (245, 110)], fill=wood_main)  # Top rail
    
    # Horizontal slats
    for y in [125, 150, 175]:
        draw.rectangle([(155, y), (245, y+8)], fill=wood_main)
        draw.line([(155, y), (245, y)], fill=wood_light)  # Top highlight
        draw.line([(155, y+8), (245, y+8)], fill=wood_dark)  # Bottom shadow
    
    # Chair legs with proper perspective and tapering
    leg_positions = [
        (145, 210, 155, 290),  # Front left
        (245, 210, 255, 290),  # Front right  
        (135, 210, 145, 290),  # Back left
        (255, 210, 265, 290)   # Back right
    ]
    
    for x1, y1, x2, y2 in leg_positions:
        # Main leg
        draw.rectangle([(x1, y1), (x2, y2)], fill=wood_main)
        # Leg highlight
        draw.line([(x1, y1), (x1, y2)], fill=wood_light)
        # Leg shadow
        draw.line([(x2-1, y1), (x2-1, y2)], fill=wood_dark)
    
    # Cross-braces between legs
    draw.rectangle([(155, 250), (245, 255)], fill=wood_main)  # Front brace
    draw.rectangle([(145, 250), (155, 255)], fill=wood_main)  # Left brace
    draw.rectangle([(245, 250), (255, 255)], fill=wood_main)  # Right brace
    
    # Realistic shadows
    # Chair shadow on floor
    shadow_color = (180, 150, 120)
    shadow_points = [(120, 285), (280, 285), (290, 305), (110, 305)]
    draw.polygon(shadow_points, fill=shadow_color)
    
    # Wall shadow from chair
    wall_shadow = [(50, 80), (80, 80), (85, 200), (55, 200)]
    draw.polygon(wall_shadow, fill=(230, 230, 225))
    
    # Additional room context
    # Window frame on left wall
    draw.rectangle([(10, 50), (40, 150)], fill=(255, 255, 255))
    draw.rectangle([(15, 55), (35, 145)], fill=(200, 230, 255))  # Window
    draw.line([(25, 55), (25, 145)], fill=(180, 180, 180))  # Window divider
    
    # Baseboard
    draw.rectangle([(0, 280), (400, 295)], fill=(255, 255, 255))
    
    # Light reflection on chair
    draw.ellipse([(160, 130), (180, 140)], fill=(wood_light[0]+20, wood_light[1]+15, wood_light[2]+10))
    
    return img

def main():
    """Main function with user-friendly interface"""
    print("🪑 Chair Video/Image Creator for Object Detection Testing")
    print("=" * 60)
    
    # Check command line arguments
    if len(sys.argv) > 1:
        if sys.argv[1] == '--image':
            create_chair_image()
            return
        elif sys.argv[1] == '--help':
            print("Usage:")
            print("  python create_chair_video.py           # Create video")
            print("  python create_chair_video.py --image   # Create single image")
            print("  python create_chair_video.py --help    # Show this help")
            return
    
    # Interactive mode
    print("What would you like to create?")
    print("1. Video with animated chair (10 seconds)")
    print("2. Single test image with chair")
    print("3. Both video and image")
    
    choice = input("\nEnter choice (1/2/3): ").strip()
    
    if choice == '1':
        success = create_chair_video()
        if success:
            print("\n🎉 Done! You can now test object detection with:")
            print("   python TRYME.py --input chair_video.mp4")
    
    elif choice == '2':
        create_chair_image()
        print("\n🎉 Done! You can now test object detection with:")
        print("   python TRYME.py --input chair_test.jpg --save-image")
    
    elif choice == '3':
        create_chair_image()
        success = create_chair_video()
        if success:
            print("\n🎉 Done! You can now test object detection with:")
            print("   python TRYME.py --input chair_test.jpg --save-image")
            print("   python TRYME.py --input chair_video.mp4")
    
    else:
        print("❌ Invalid choice. Use --help for options.")

if __name__ == "__main__":
    main()