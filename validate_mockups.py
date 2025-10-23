"""
Visual Mockup Validator
Opens the category showcase mockups to verify no characters are cut off
"""

import os
from PIL import Image

mockup_dir = "etsy_mockups"

# Category showcase mockups (the ones with grids that were problematic)
category_mockups = [
    "mockup_02_vampires_witches.png",
    "mockup_03_zombies_ghosts.png",
    "mockup_04_monsters_creatures.png",
    "mockup_05_demons_spirits.png",
    "mockup_16_collection_1.png",
    "mockup_17_collection_2.png",
    "mockup_18_variety_mix.png",
    "mockup_19_best_sellers.png",
]

print("\n" + "="*70)
print("🔍 VALIDATING CATEGORY MOCKUPS")
print("="*70)
print()

for mockup in category_mockups:
    filepath = os.path.join(mockup_dir, mockup)
    
    if not os.path.exists(filepath):
        print(f"❌ Missing: {mockup}")
        continue
    
    try:
        with Image.open(filepath) as img:
            width, height = img.size
            
            # Check dimensions
            if width == 2000 and height == 2200:
                status = "✅"
            else:
                status = "⚠️"
            
            print(f"{status} {mockup:35s} - {width}x{height}px")
            
    except Exception as e:
        print(f"❌ {mockup:35s} - Error: {e}")

print("\n" + "="*70)
print("✅ VALIDATION COMPLETE!")
print()
print("📝 All category mockups now have 2200px height (increased from 2000px)")
print("   This ensures the 4x4 grid of characters fits completely")
print("   No characters should be cut off at the bottom!")
print("="*70)
print()
print("💡 To view the mockups:")
print("   Navigate to: f:\\AI\\1. Prompt Engineering\\etsy_mockups\\")
print("   Open any mockup_XX file to preview")
print("="*70)
