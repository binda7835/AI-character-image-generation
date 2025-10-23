"""
Optimize PNG Files for Etsy Upload
Reduces file size while maintaining quality
Etsy requires individual files under 20 MB
"""

import os
from PIL import Image
from pathlib import Path

def optimize_png_for_etsy(input_dir, output_dir):
    """
    Optimize PNG files to be under 20 MB each while keeping quality
    """
    
    os.makedirs(output_dir, exist_ok=True)
    
    print("\n" + "="*70)
    print("🔧 OPTIMIZING PNG FILES FOR ETSY")
    print("="*70)
    print()
    print("Etsy requirement: Each file must be under 20 MB")
    print("Current files: ~8-10 MB each (should be fine, but let's optimize)")
    print()
    
    png_files = sorted([f for f in os.listdir(input_dir) if f.endswith('.png')])
    
    if not png_files:
        print(f"❌ No PNG files found in {input_dir}")
        return
    
    print(f"Found {len(png_files)} files to optimize\n")
    
    total_original = 0
    total_optimized = 0
    
    for i, filename in enumerate(png_files, 1):
        input_path = os.path.join(input_dir, filename)
        output_path = os.path.join(output_dir, filename)
        
        # Get original size
        original_size = os.path.getsize(input_path) / (1024 * 1024)  # MB
        total_original += original_size
        
        # Open and optimize
        with Image.open(input_path) as img:
            # Save with optimal compression
            img.save(
                str(output_path),
                'PNG',
                optimize=True,
                compress_level=9  # Maximum compression
            )
        
        # Get new size
        new_size = os.path.getsize(output_path) / (1024 * 1024)  # MB
        total_optimized += new_size
        
        reduction = ((original_size - new_size) / original_size) * 100
        
        if new_size < 20:
            status = "✅"
        else:
            status = "⚠️"
        
        print(f"{status} {i:3d}/100 {filename:35s} {original_size:6.2f}MB → {new_size:6.2f}MB ({reduction:4.1f}% smaller)")
    
    print("\n" + "="*70)
    print("✅ OPTIMIZATION COMPLETE!")
    print("="*70)
    print(f"Original total size: {total_original:.2f} MB")
    print(f"Optimized total size: {total_optimized:.2f} MB")
    print(f"Total reduction: {((total_original - total_optimized) / total_original * 100):.1f}%")
    print(f"Average file size: {total_optimized / len(png_files):.2f} MB")
    print("="*70)


if __name__ == "__main__":
    input_directory = "halloween_characters_transparent"
    output_directory = "halloween_characters_optimized"
    
    optimize_png_for_etsy(input_directory, output_directory)
    
    print("\n📝 Next step: Create ZIP with optimized files")
    print("   The optimized files are in:", output_directory)
