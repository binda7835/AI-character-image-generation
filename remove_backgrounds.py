"""
High-Quality Background Removal Script for Halloween Characters
Makes all 100 PNG images have transparent backgrounds
Uses remove.bg API (50 free images/month) for professional results
NO COMPROMISE ON QUALITY - Professional AI background removal
"""

import os
import requests
import json
from pathlib import Path

def remove_bg_api(input_path, output_path, api_key):
    """Remove background using remove.bg API (Professional Quality)"""
    
    try:
        with open(input_path, 'rb') as img_file:
            response = requests.post(
                'https://api.remove.bg/v1.0/removebg',
                files={'image_file': img_file},
                data={
                    'size': 'full',  # Full resolution - NO COMPROMISE
                    'format': 'png',
                    'type': 'auto',
                },
                headers={'X-Api-Key': api_key},
                timeout=60
            )
        
        if response.status_code == requests.codes.ok:
            with open(output_path, 'wb') as out_file:
                out_file.write(response.content)
            return True, None
        else:
            return False, f"Error {response.status_code}: {response.text}"
            
    except Exception as e:
        return False, str(e)


def remove_background_from_images(api_key, input_dir="halloween_characters", output_dir="halloween_characters_transparent"):
    """Remove background from all images using remove.bg API"""
    
    # Create output directory
    os.makedirs(output_dir, exist_ok=True)
    
    # Get all PNG files
    png_files = sorted(Path(input_dir).glob("halloween_character_*.png"))
    
    total = len(png_files)
    print(f"\n{'='*70}")
    print(f"🎃 HIGH-QUALITY BACKGROUND REMOVAL - BATCH PROCESSOR")
    print(f"{'='*70}")
    print(f"📁 Input: {input_dir}")
    print(f"📁 Output: {output_dir}")
    print(f"🖼️  Total images: {total}")
    print(f"🔑 API: remove.bg (Professional Quality)")
    print(f"💰 Cost: FREE for first 50 images/month\n")
    
    successful = 0
    failed = 0
    skipped = 0
    
    for i, img_path in enumerate(png_files, 1):
        filename = img_path.name
        output_path = os.path.join(output_dir, filename)
        
        # Skip if already processed
        if os.path.exists(output_path):
            print(f"⏭️  [{i}/{total}] Skipping (already exists): {filename}")
            skipped += 1
            continue
        
        print(f"🔄 [{i}/{total}] Processing: {filename}...", end=' ')
        
        success, error = remove_bg_api(str(img_path), output_path, api_key)
        
        if success:
            print(f"✅ Done!")
            successful += 1
        else:
            print(f"❌ Failed!")
            if error:
                print(f"    Error: {error}")
            failed += 1
        
        # Progress updates
        if successful > 0 and successful % 10 == 0:
            print(f"\n📊 Progress: {successful} images completed")
            if successful >= 45:
                print(f"⚠️  Warning: Approaching free tier limit (50/month)\n")
    
    print(f"\n{'='*70}")
    print(f"✅ Successfully processed: {successful}")
    print(f"⏭️  Skipped (already done): {skipped}")
    print(f"❌ Failed: {failed}")
    print(f"📁 Transparent images saved in: {output_dir}")
    print(f"{'='*70}")




def main():
    """Main execution"""
    print("\n" + "="*70)
    print("🎃 HIGH-QUALITY BACKGROUND REMOVAL - remove.bg API")
    print("="*70)
    
    # Try to load API key from config
    api_key = None
    try:
        with open('config.json', 'r') as f:
            config = json.load(f)
            api_key = config.get('removebg_api_key', '')
            if not api_key or api_key.startswith('YOUR_'):
                api_key = None
    except:
        pass
    
    if not api_key:
        print("\n⚠️  NO API KEY CONFIGURED")
        print("\n🆓 GET FREE API KEY (50 images/month - Professional Quality):")
        print("=" * 70)
        print("1. Go to: https://www.remove.bg/users/sign_up")
        print("2. Sign up for FREE account (no credit card required)")
        print("3. Get API key from: https://www.remove.bg/api#remove-background")
        print("4. Copy your API key")
        print("5. Edit config.json and add:")
        print('   "removebg_api_key": "YOUR_API_KEY_HERE"')
        print("\n💎 Quality: Professional AI - NO COMPROMISE")
        print("💰 Cost: FREE for first 50 images/month")
        print("⚡ Speed: ~3-5 seconds per image")
        print("🎯 Perfect for: Print quality, commercial use")
        print("=" * 70)
        
        print("\n📝 Or enter your API key now:")
        user_input = input("API Key (or press Enter to exit): ").strip()
        
        if user_input:
            api_key = user_input
        else:
            print("\n👋 Exiting. Get your free API key and run again!")
            return
    
    # Run the background removal
    remove_background_from_images(api_key)


if __name__ == "__main__":
    main()
