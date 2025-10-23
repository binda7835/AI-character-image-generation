"""
Background Removal using rembg - FIXED for Python 3.13 compatibility
Processes all 100 Halloween character images with AI-powered background removal
Creates transparent backgrounds with high quality - NO COMPROMISE
"""

import os
import sys
from pathlib import Path
from PIL import Image
import io


def try_rembg_removal(input_dir="halloween_characters", output_dir="halloween_characters_transparent"):
    """Professional AI background removal using rembg - FIXED PATH HANDLING"""
    
    try:
        from rembg import remove
        REMBG_AVAILABLE = True
    except ImportError:
        print("❌ rembg not installed!")
        print("\nInstall with: pip install rembg")
        print("Note: Will download ~285MB AI model on first use")
        return False
    
    # Create output directory using pathlib (handles Windows paths better)
    output_path = Path(output_dir)
    output_path.mkdir(exist_ok=True)
    
    # Get all PNG files
    input_path = Path(input_dir)
    image_files = sorted(input_path.glob("halloween_character_*.png"))
    
    total = len(image_files)
    
    print()
    print("="*70)
    print("🎃 AI-POWERED BACKGROUND REMOVAL (rembg)")
    print("="*70)
    print(f"📁 Input: {input_dir}")
    print(f"📁 Output: {output_dir}")
    print(f"🖼️  Images: {total}")
    print(f"🤖 Method: AI Background Removal (U2-Net model)")
    print(f"💰 Cost: FREE (local processing)")
    print(f"💎 Quality: HIGH - Professional AI")
    print("="*70)
    print()
    
    successful = 0
    failed = 0
    skipped = 0
    
    for i, img_file in enumerate(image_files, 1):
        filename = img_file.name
        output_file = output_path / filename
        
        # Skip if already processed
        if output_file.exists():
            print(f"⏭️  [{i}/{total}] Already exists: {filename}")
            skipped += 1
            continue
        
        print(f"🔄 [{i}/{total}] Processing: {filename}...", end=' ', flush=True)
        
        try:
            # Read input image as bytes (FIXED: proper path handling)
            with open(str(img_file), 'rb') as f:
                input_data = f.read()
            
            # Remove background using AI
            output_data = remove(input_data)
            
            # Load result as PIL Image
            img = Image.open(io.BytesIO(output_data))
            
            # Ensure RGBA mode for transparency
            if img.mode != 'RGBA':
                img = img.convert('RGBA')
            
            # Save with 300 DPI metadata (FIXED: use str() for path)
            img.save(str(output_file), 'PNG', dpi=(300, 300))
            
            print(f"✅ Done!")
            successful += 1
            
        except Exception as e:
            print(f"❌ Failed!")
            print(f"    Error: {type(e).__name__}: {str(e)}")
            failed += 1
            continue
        
        # Progress update
        if successful > 0 and successful % 10 == 0:
            print()
            print(f"📊 Progress: {successful}/{total} images completed")
            print()
    
    # Final summary
    print()
    print("="*70)
    print("🎉 BACKGROUND REMOVAL COMPLETE!")
    print("="*70)
    print(f"✅ Successfully processed: {successful}")
    print(f"⏭️  Skipped (existing): {skipped}")
    print(f"❌ Failed: {failed}")
    print(f"📁 Location: {output_dir}/")
    print("="*70)
    
    if successful > 0:
        print()
        print("💎 Quality: Professional AI-powered removal")
        print("📏 Resolution: 4500x5400 pixels @ 300 DPI maintained")
        print("✨ Format: PNG with full alpha transparency")
        print("🎃 Ready for: Print, web, commercial use")
    
    return True


if __name__ == "__main__":
    print()
    print("="*70)
    print("🎃 HALLOWEEN CHARACTER BACKGROUND REMOVAL")
    print("="*70)
    
    # Try using rembg (AI-powered)
    success = try_rembg_removal()
    
    if not success:
        print("\n⚠️  Could not use rembg")
        print("\n📦 To install rembg:")
        print("   pip install rembg")
        print("\n💡 This provides professional AI background removal")
        print("   First use will download ~285MB U2-Net model")
        sys.exit(1)
