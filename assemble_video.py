"""
Etsy Video Creator (Alternative Method using MoviePy)
Creates a complete MP4 video from frames if moviepy is installed
"""

import os
from pathlib import Path

def create_video_with_moviepy():
    """Create video using moviepy library"""
    try:
        from moviepy.editor import ImageSequenceClip
        print("✓ MoviePy found!")
    except ImportError:
        print("❌ MoviePy not installed")
        print("\nTo install MoviePy:")
        print("  pip install moviepy")
        print("\nOr use the create_video_frames.py method and assemble manually")
        return
    
    frames_dir = "video_frames"
    output_file = "etsy_preview_video.mp4"
    
    if not os.path.exists(frames_dir):
        print(f"❌ Frames directory not found: {frames_dir}")
        print("Run create_video_frames.py first!")
        return
    
    # Get all frame files
    frame_files = sorted([
        os.path.join(frames_dir, f) 
        for f in os.listdir(frames_dir) 
        if f.endswith('.png')
    ])
    
    if not frame_files:
        print("❌ No frames found!")
        return
    
    print("\n" + "="*70)
    print("🎬 CREATING VIDEO WITH MOVIEPY")
    print("="*70)
    print(f"📊 Total frames: {len(frame_files)}")
    print(f"⏱️ FPS: 30")
    print(f"⏰ Duration: {len(frame_files)/30:.1f} seconds")
    print("="*70)
    print()
    
    # Create video
    print("⏳ Processing video (this may take a few minutes)...")
    clip = ImageSequenceClip(frame_files, fps=30)
    clip.write_videofile(output_file, codec='libx264', fps=30)
    
    print("\n" + "="*70)
    print("✅ VIDEO CREATED!")
    print(f"📁 File: {output_file}")
    print(f"📊 Size: {os.path.getsize(output_file) / (1024*1024):.2f} MB")
    print("="*70)


def create_simple_gif():
    """Create an animated GIF as alternative to video"""
    try:
        from PIL import Image
    except ImportError:
        print("❌ Pillow not installed")
        return
    
    frames_dir = "video_frames"
    output_file = "etsy_preview_animation.gif"
    
    if not os.path.exists(frames_dir):
        print(f"❌ Frames directory not found: {frames_dir}")
        return
    
    # Get every 5th frame to make smaller GIF (6 FPS instead of 30)
    frame_files = sorted([
        os.path.join(frames_dir, f) 
        for f in os.listdir(frames_dir) 
        if f.endswith('.png')
    ])[::5]  # Every 5th frame
    
    if not frame_files:
        print("❌ No frames found!")
        return
    
    print("\n" + "="*70)
    print("🎨 CREATING ANIMATED GIF")
    print("="*70)
    print(f"📊 Using {len(frame_files)} frames")
    print("="*70)
    print()
    
    # Load frames
    frames = []
    for i, frame_file in enumerate(frame_files):
        print(f"⏳ Loading frame {i+1}/{len(frame_files)}...")
        frames.append(Image.open(frame_file))
    
    # Save as GIF
    print("💾 Saving GIF...")
    frames[0].save(
        output_file,
        save_all=True,
        append_images=frames[1:],
        duration=167,  # ~6 FPS (1000ms / 6)
        loop=0
    )
    
    print("\n" + "="*70)
    print("✅ ANIMATED GIF CREATED!")
    print(f"📁 File: {output_file}")
    print(f"📊 Size: {os.path.getsize(output_file) / (1024*1024):.2f} MB")
    print("\n📝 Note: Etsy prefers MP4 videos, but GIF works for previews")
    print("="*70)


if __name__ == "__main__":
    print("Choose method:")
    print("1. Create MP4 video (requires moviepy)")
    print("2. Create animated GIF (requires only Pillow)")
    print()
    
    choice = input("Enter choice (1 or 2): ").strip()
    
    if choice == "1":
        create_video_with_moviepy()
    elif choice == "2":
        create_simple_gif()
    else:
        print("Invalid choice. Creating GIF by default...")
        create_simple_gif()
