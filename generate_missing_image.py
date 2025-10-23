"""
Quick script to generate a single missing Halloween character image
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
    "output_dir": "halloween_characters"
}

# Load prompts
with open('halloween_prompts.json', 'r') as f:
    prompts = json.load(f)

# Get prompt #75
prompt_data = prompts[74]  # Index 74 for image 75
prompt = prompt_data['prompt']
index = 75

print(f"Generating missing image #{index}...")
print(f"Prompt: {prompt}")

# Enhanced prompt
enhanced_prompt = f"{prompt}, white background, isolated character, professional photography, 8K, ultra detailed, masterpiece"
encoded_prompt = urllib.parse.quote(enhanced_prompt)

# Pollinations.ai API
image_url = f"https://image.pollinations.ai/prompt/{encoded_prompt}?width=1024&height=1024&nologo=true&enhance=true"

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
        
        print(f"✓ Successfully saved: {output_path}")
        print(f"\n🎉 You now have 100 complete Halloween character images!")
    else:
        print(f"✗ Error {response.status_code}: Failed to generate image")
        
except Exception as e:
    print(f"✗ Exception: {str(e)}")
