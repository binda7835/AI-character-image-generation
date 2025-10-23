"""
Quick Background Removal - No external dependencies
Uses PIL only to remove white backgrounds
"""

import os
from PIL import Image

def make_transparent_simple(input_dir="halloween_characters", output_dir="halloween_characters_transparent"):
    """Remove white backgrounds using PIL only"""
    
    os.makedirs(output_dir, exist_ok=True)
    
    image_files = [f for f in os.listdir(input_dir) if f.endswith('.png')]
    image_files.sort()
    
    print(f"Processing {len(image_files)} images...")
    print(f"Input: {input_dir}")
    print(f"Output: {output_dir}\n")
    
    successful = 0
    failed = 0
    
    for i, filename in enumerate(image_files, 1):
        try:
            input_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, filename)
            
            # Open image
            img = Image.open(input_path)
            img = img.convert("RGBA")
            
            # Get pixel data
            pixels = img.load()
            width, height = img.size
            
            # Make white/light pixels transparent
            threshold = 240  # Adjust: higher = more aggressive (240-250 recommended)
            
            for y in range(height):
                for x in range(width):
                    r, g, b, a = pixels[x, y]
                    # If pixel is very light/white
                    if r > threshold and g > threshold and b > threshold:
                        pixels[x, y] = (r, g, b, 0)  # Make transparent
            
            # Save with DPI
            img.save(output_path, "PNG", dpi=(300, 300))
            
            successful += 1
            print(f"✓ [{i}/{len(image_files)}] {filename}")
            
        except Exception as e:
            print(f"✗ [{i}/{len(image_files)}] Error: {str(e)}")
            failed += 1
    
    print(f"\n{'='*60}")
    print(f"Complete! Successful: {successful}, Failed: {failed}")
    print(f"Output: {output_dir}/")
    print(f"{'='*60}")

if __name__ == "__main__":
    print("="*60)
    print("Halloween Background Removal (Simple Method)")
    print("="*60)
    print()
    make_transparent_simple()
