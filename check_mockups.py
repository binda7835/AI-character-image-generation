"""
Quick Preview of Mockup Files
Shows which mockups have been created and their sizes
"""

import os
from PIL import Image

mockup_dir = "etsy_mockups"

print("\n" + "="*70)
print("📸 MOCKUP FILES STATUS")
print("="*70)
print()

if not os.path.exists(mockup_dir):
    print(f"❌ Directory not found: {mockup_dir}")
    exit()

mockup_files = sorted([f for f in os.listdir(mockup_dir) if f.endswith('.png')])

if not mockup_files:
    print("❌ No mockup files found!")
    exit()

print(f"✓ Found {len(mockup_files)} mockup files:\n")

total_size = 0
for i, filename in enumerate(mockup_files, 1):
    filepath = os.path.join(mockup_dir, filename)
    file_size = os.path.getsize(filepath) / (1024 * 1024)  # MB
    total_size += file_size
    
    # Get image dimensions
    try:
        with Image.open(filepath) as img:
            width, height = img.size
            print(f"{i:2d}. {filename:35s} - {width}x{height}px - {file_size:.2f} MB")
    except Exception as e:
        print(f"{i:2d}. {filename:35s} - Error: {e}")

print()
print("="*70)
print(f"✅ Total: {len(mockup_files)} files, {total_size:.2f} MB")
print("="*70)

# Check if all 20 are there
if len(mockup_files) == 20:
    print("\n✅ ALL 20 MOCKUPS CREATED SUCCESSFULLY!")
else:
    print(f"\n⚠️  Expected 20 mockups, found {len(mockup_files)}")
    print("   Still generating...")
