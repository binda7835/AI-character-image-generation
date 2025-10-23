"""
Generate Specific Halloween Character Images
Regenerates only specified image numbers with new prompts
"""

import os
import json
import requests
from PIL import Image
from io import BytesIO
import urllib.parse

# Configuration
CONFIG = {
    "width": 4500,
    "height": 5400,
    "dpi": 300,
    "output_dir": "halloween_characters",
    "api_choice": "pollinations"
}

# Image numbers to regenerate
IMAGE_NUMBERS = [3, 23]

def generate_image(prompt, index):
    """Generate a single image using Pollinations.ai"""
    
    # Enhanced prompt
    enhanced_prompt = f"{prompt}, white background, isolated character, professional photography, 8K, ultra detailed, masterpiece"
    encoded_prompt = urllib.parse.quote(enhanced_prompt)
    
    # Pollinations.ai free API
    image_url = f"https://image.pollinations.ai/prompt/{encoded_prompt}?width=1024&height=1024&nologo=true&enhance=true"
    
    print(f"🔄 Generating image {index}: {prompt[:60]}...")
    
    try:
        # Download the generated image
        response = requests.get(image_url, timeout=120)
        
        if response.status_code == 200:
            # Load image
            image = Image.open(BytesIO(response.content))
            
            # Resize to exact dimensions
            image = image.resize((CONFIG['width'], CONFIG['height']), Image.Resampling.LANCZOS)
            
            # Convert to RGBA for transparency support
            if image.mode != 'RGBA':
                image = image.convert('RGBA')
            
            # Save with DPI metadata
            output_path = os.path.join(CONFIG['output_dir'], f"halloween_character_{index:03d}.png")
            image.save(output_path, "PNG", dpi=(CONFIG['dpi'], CONFIG['dpi']))
            
            print(f"✅ Saved: {output_path}")
            return True
        else:
            print(f"❌ Error {response.status_code}: Failed to generate image")
            return False
            
    except Exception as e:
        print(f"❌ Exception: {str(e)}")
        return False


def main():
    """Generate specific images"""
    print("\n" + "="*70)
    print("🎃 REGENERATING SPECIFIC HALLOWEEN CHARACTERS")
    print("="*70)
    
    # Load prompts
    with open('halloween_prompts.json', 'r') as f:
        prompts = json.load(f)
    
    print(f"📝 Images to regenerate: {IMAGE_NUMBERS}")
    print(f"🎨 Using: Pollinations.ai (FREE)")
    print(f"📏 Resolution: {CONFIG['width']}x{CONFIG['height']} @ {CONFIG['dpi']} DPI")
    print("="*70)
    print()
    
    successful = 0
    failed = 0
    
    for img_num in IMAGE_NUMBERS:
        prompt_data = prompts[img_num - 1]  # Index is 0-based
        prompt = prompt_data['prompt']
        
        print(f"\n🎃 Image #{img_num}")
        print(f"📝 New character: {prompt}")
        
        success = generate_image(prompt, img_num)
        
        if success:
            successful += 1
        else:
            failed += 1
    
    print("\n" + "="*70)
    print(f"✅ Successfully generated: {successful}")
    print(f"❌ Failed: {failed}")
    print("="*70)
    
    if successful > 0:
        print("\n🎃 Next step: Run make_transparent.py to remove backgrounds")


if __name__ == "__main__":
    main()
