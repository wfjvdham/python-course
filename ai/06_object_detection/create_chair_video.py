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
    """Create a single frame with a chair drawing"""
    
    # Create image with background
    img = Image.new('RGB', (width, height), color=(135, 206, 235))  # Sky blue
    draw = ImageDraw.Draw(img)
    
    # Draw floor
    floor_y = height - 100
    draw.rectangle([0, floor_y, width, height], fill=(34, 139, 34))  # Forest green
    
    # Animate chair position (simple left-right movement)
    animation_progress = frame_number / total_frames
    chair_x = int(width * 0.2 + (width * 0.6) * (0.5 + 0.5 * abs(2 * animation_progress - 1)))
    chair_y = floor_y - 120
    
    # Chair dimensions
    chair_width = 80
    chair_height = 120
    
    # Draw chair shadow
    shadow_offset = 10
    draw.ellipse([
        chair_x + shadow_offset, chair_y + chair_height + 5,
        chair_x + chair_width + shadow_offset + 20, chair_y + chair_height + 25
    ], fill=(0, 100, 0, 128))  # Semi-transparent dark green
    
    # Draw chair seat
    seat_color = (139, 69, 19)  # Brown
    draw.rectangle([
        chair_x + 10, chair_y + 40,
        chair_x + chair_width - 10, chair_y + 60
    ], fill=seat_color, outline=(101, 67, 33), width=2)
    
    # Draw chair back
    draw.rectangle([
        chair_x + 15, chair_y,
        chair_x + chair_width - 15, chair_y + 50
    ], fill=seat_color, outline=(101, 67, 33), width=2)
    
    # Draw chair legs
    leg_width = 6
    leg_color = seat_color
    
    # Front legs
    draw.rectangle([
        chair_x + 15, chair_y + 60,
        chair_x + 15 + leg_width, chair_y + chair_height
    ], fill=leg_color)
    
    draw.rectangle([
        chair_x + chair_width - 15 - leg_width, chair_y + 60,
        chair_x + chair_width - 15, chair_y + chair_height
    ], fill=leg_color)
    
    # Back legs
    draw.rectangle([
        chair_x + 20, chair_y + 60,
        chair_x + 20 + leg_width, chair_y + chair_height
    ], fill=leg_color)
    
    draw.rectangle([
        chair_x + chair_width - 20 - leg_width, chair_y + 60,
        chair_x + chair_width - 20, chair_y + chair_height
    ], fill=leg_color)
    
    # Add some decorative elements
    # Sun
    sun_x, sun_y = width - 80, 60
    draw.ellipse([sun_x - 30, sun_y - 30, sun_x + 30, sun_y + 30], fill=(255, 255, 0))
    
    # Clouds
    cloud_offset = (frame_number * 0.5) % (width + 100) - 50
    draw.ellipse([cloud_offset, 40, cloud_offset + 60, 80], fill=(255, 255, 255))
    draw.ellipse([cloud_offset + 20, 30, cloud_offset + 80, 70], fill=(255, 255, 255))
    
    # Add frame counter and info text
    try:
        # Try to use default font
        font = ImageFont.load_default()
    except:
        font = None
    
    text_color = (255, 255, 255)
    draw.text((10, 10), f"Frame: {frame_number}/{total_frames}", fill=text_color, font=font)
    draw.text((10, height - 30), "Chair Detection Test Video", fill=text_color, font=font)
    
    return img

def create_chair_video(output_filename="chair_video.mp4", duration=10, fps=25):
    """Create a video with animated chair"""
    
    total_frames = duration * fps
    temp_dir = "temp_frames"
    
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
            output_filename
        ]
        
        try:
            result = subprocess.run(cmd, capture_output=True, text=True)
            if result.returncode == 0:
                print(f"✅ Video created successfully: {output_filename}")
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
        print(f"   ffmpeg -framerate {fps} -i {temp_dir}/frame_%06d.png -c:v libx264 {output_filename}")
        return False
    
    # Cleanup temp files
    print("🧹 Cleaning up temporary files...")
    import shutil
    shutil.rmtree(temp_dir)
    
    return True

def create_chair_image(filename="chair_test.jpg"):
    """Create a single test image with a chair"""
    print(f"📸 Creating test image: {filename}")
    
    frame = create_chair_frame(125, 250)  # Middle frame position
    frame.save(filename)
    
    print(f"✅ Test image created: {filename}")
    return True

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