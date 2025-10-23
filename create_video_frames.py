"""
Etsy Preview Video Generator
Creates a 15-second preview video showing Halloween characters
Displays characters in a dynamic slideshow format
"""

import os
from PIL import Image, ImageDraw, ImageFont
import random

def create_video_frames():
    """Create frames for a 15-second video at 30 FPS = 450 frames"""
    
    input_dir = "halloween_characters_transparent"
    output_dir = "video_frames"
    os.makedirs(output_dir, exist_ok=True)
    
    width = 1920
    height = 1080
    fps = 30
    duration = 15  # seconds
    total_frames = fps * duration
    
    # Select 15 characters to show (1 per second)
    character_numbers = [1, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 60, 70, 80, 90]
    frames_per_char = fps  # 30 frames per character (1 second each)
    
    print("\n" + "="*70)
    print("🎬 GENERATING VIDEO FRAMES")
    print("="*70)
    print(f"📹 Resolution: {width}x{height}")
    print(f"⏱️ Duration: {duration} seconds")
    print(f"🎞️ FPS: {fps}")
    print(f"📊 Total frames: {total_frames}")
    print("="*70)
    print()
    
    frame_num = 0
    
    for char_idx, char_num in enumerate(character_numbers):
        # Load character
        img_path = os.path.join(input_dir, f"halloween_character_{char_num:03d}.png")
        
        if not os.path.exists(img_path):
            print(f"⚠️  Skipping character {char_num} - file not found")
            continue
        
        char_img = Image.open(img_path)
        
        # Create frames for this character
        for i in range(frames_per_char):
            # Create background
            # Gradient background colors
            colors = ['#1a0033', '#330066', '#4d0099', '#6600cc', '#7f00ff']
            bg_color = colors[char_idx % len(colors)]
            
            frame = Image.new('RGB', (width, height), bg_color)
            draw = ImageDraw.Draw(frame)
            
            # Scale and position character
            char_size = 800
            char_resized = char_img.resize((char_size, char_size), Image.Resampling.LANCZOS)
            
            # Center character
            char_x = (width - char_size) // 2
            char_y = (height - char_size) // 2
            
            # Add character
            if char_resized.mode == 'RGBA':
                frame.paste(char_resized, (char_x, char_y), char_resized)
            else:
                frame.paste(char_resized, (char_x, char_y))
            
            # Add text overlay
            try:
                title_font = ImageFont.truetype("arialbd.ttf", 80)
                subtitle_font = ImageFont.truetype("arial.ttf", 50)
            except:
                title_font = ImageFont.load_default()
                subtitle_font = title_font
            
            # Title at top
            draw.text((width//2, 80), "100 Halloween Characters", 
                     fill='white', font=title_font, anchor='mm')
            
            # Character number
            draw.text((width//2, height - 100), f"Character #{char_num}", 
                     fill='#ff6b00', font=subtitle_font, anchor='mm')
            
            # Progress indicator
            progress_width = 1600
            progress_x = (width - progress_width) // 2
            progress_y = height - 50
            
            # Background bar
            draw.rectangle([(progress_x, progress_y), (progress_x + progress_width, progress_y + 20)], 
                          fill='#333333')
            
            # Progress bar
            progress = (char_idx * frames_per_char + i) / total_frames
            progress_filled = int(progress_width * progress)
            draw.rectangle([(progress_x, progress_y), (progress_x + progress_filled, progress_y + 20)], 
                          fill='#ff6b00')
            
            # Save frame
            frame_path = os.path.join(output_dir, f"frame_{frame_num:04d}.png")
            frame.save(frame_path, 'PNG')
            
            if frame_num % 30 == 0:  # Print every second
                print(f"⏳ Generated {frame_num}/{total_frames} frames ({frame_num//30}s)...")
            
            frame_num += 1
    
    print("\n" + "="*70)
    print(f"✅ GENERATED {frame_num} FRAMES")
    print(f"📁 Location: {output_dir}/")
    print("\n📝 TO CREATE VIDEO:")
    print("="*70)
    print("Option 1 - Using FFmpeg (if installed):")
    print(f'  ffmpeg -framerate 30 -i {output_dir}/frame_%04d.png -c:v libx264 -pix_fmt yuv420p etsy_preview.mp4')
    print("\nOption 2 - Use online tools:")
    print("  1. Upload frames to: https://www.online-convert.com/")
    print("  2. Or use: https://ezgif.com/png-to-mp4")
    print("  3. Set FPS to 30")
    print("\nOption 3 - Use video editing software:")
    print("  Import frame sequence into:")
    print("  - Adobe Premiere Pro")
    print("  - DaVinci Resolve (FREE)")
    print("  - iMovie")
    print("  - Windows Photos/Movie Maker")
    print("="*70)


if __name__ == "__main__":
    create_video_frames()
