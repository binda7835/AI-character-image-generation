"""
Quick Etsy Preview Creator
Creates a simple but effective preview GIF showing your characters
Much faster than full video - perfect for Etsy!
"""

import os
from PIL import Image, ImageDraw, ImageFont
import random

def create_quick_preview():
    """Create a quick animated preview of characters"""
    
    input_dir = "halloween_characters_transparent"
    output_file = "etsy_preview.gif"
    
    # Etsy-optimized settings
    width = 1600
    height = 1200
    
    print("\n" + "="*70)
    print("🎨 CREATING QUICK ETSY PREVIEW GIF")
    print("="*70)
    print()
    
    # Select 20 characters to showcase (every 5th character)
    character_numbers = list(range(1, 101, 5))[:20]
    frames = []
    
    for i, char_num in enumerate(character_numbers):
        print(f"⏳ Creating frame {i+1}/20 (Character {char_num})...")
        
        # Create frame with gradient background
        colors = [
            ('#1a0033', '#4d0099'),  # Purple
            ('#0d1b2a', '#1b263b'),  # Dark blue
            ('#14213d', '#fca311'),  # Blue-orange
            ('#000000', '#8b00ff'),  # Black-purple
            ('#1a1a1a', '#ff6b00'),  # Dark-orange
        ]
        bg1, bg2 = colors[i % len(colors)]
        
        frame = Image.new('RGB', (width, height), bg1)
        draw = ImageDraw.Draw(frame)
        
        # Add gradient effect (simplified)
        for y in range(height):
            color = bg1 if y < height // 2 else bg2
            draw.line([(0, y), (width, y)], fill=color, width=1)
        
        # Load character
        img_path = os.path.join(input_dir, f"halloween_character_{char_num:03d}.png")
        
        if os.path.exists(img_path):
            try:
                with Image.open(img_path) as char_img:
                    # Resize character
                    char_img.thumbnail((800, 800), Image.Resampling.LANCZOS)
                    
                    # Center character
                    char_x = (width - char_img.width) // 2
                    char_y = (height - char_img.height) // 2
                    
                    # Paste character
                    if char_img.mode == 'RGBA':
                        frame.paste(char_img, (char_x, char_y), char_img)
                    else:
                        frame.paste(char_img, (char_x, char_y))
            except Exception as e:
                print(f"⚠️  Error loading character {char_num}: {e}")
        
        # Add text overlay
        try:
            title_font = ImageFont.truetype("arialbd.ttf", 60)
            subtitle_font = ImageFont.truetype("arial.ttf", 40)
        except:
            title_font = ImageFont.load_default()
            subtitle_font = title_font
        
        # Title
        draw.text((width//2, 50), "100 Halloween Characters Bundle", 
                 fill='white', font=title_font, anchor='mm')
        
        # Character number
        draw.text((width//2, height - 50), f"Character #{char_num} of 100", 
                 fill='#ff6b00', font=subtitle_font, anchor='mm')
        
        # Add to frames
        frames.append(frame.copy())
    
    # Save as GIF
    print("\n💾 Saving animated GIF...")
    frames[0].save(
        output_file,
        save_all=True,
        append_images=frames[1:],
        duration=750,  # 0.75 seconds per frame = 15 second total
        loop=0,
        optimize=True
    )
    
    file_size = os.path.getsize(output_file) / (1024 * 1024)
    
    print("\n" + "="*70)
    print("✅ ETSY PREVIEW GIF CREATED!")
    print(f"📁 File: {output_file}")
    print(f"📊 Size: {file_size:.2f} MB")
    print(f"⏱️ Duration: 15 seconds")
    print(f"🎞️ Frames: 20")
    print("\n📝 READY TO UPLOAD TO ETSY!")
    print("   Etsy accepts GIF files for product previews")
    print("   Maximum file size: 10 MB (yours is {:.2f} MB)".format(file_size))
    print("="*70)


def create_showcase_grid():
    """Create a static grid showing many characters - alternative to animation"""
    
    input_dir = "halloween_characters_transparent"
    output_file = "etsy_character_grid.png"
    
    print("\n" + "="*70)
    print("🎨 CREATING CHARACTER SHOWCASE GRID")
    print("="*70)
    print()
    
    # Grid settings
    cols = 10
    rows = 10
    cell_size = 300
    width = cols * cell_size
    height = rows * cell_size
    
    # Create large canvas
    grid = Image.new('RGB', (width, height), '#2d2d2d')
    
    # Place all 100 characters
    for char_num in range(1, 101):
        row = (char_num - 1) // cols
        col = (char_num - 1) % cols
        
        x = col * cell_size
        y = row * cell_size
        
        print(f"⏳ Placing character {char_num}/100...")
        
        img_path = os.path.join(input_dir, f"halloween_character_{char_num:03d}.png")
        
        if os.path.exists(img_path):
            try:
                with Image.open(img_path) as char_img:
                    char_img.thumbnail((cell_size - 10, cell_size - 10), Image.Resampling.LANCZOS)
                    
                    # Center in cell
                    char_x = x + (cell_size - char_img.width) // 2
                    char_y = y + (cell_size - char_img.height) // 2
                    
                    if char_img.mode == 'RGBA':
                        grid.paste(char_img, (char_x, char_y), char_img)
                    else:
                        grid.paste(char_img, (char_x, char_y))
            except Exception as e:
                print(f"⚠️  Error loading character {char_num}: {e}")
    
    # Save
    print("\n💾 Saving grid image...")
    grid.save(output_file, 'PNG', optimize=True)
    
    file_size = os.path.getsize(output_file) / (1024 * 1024)
    
    print("\n" + "="*70)
    print("✅ CHARACTER GRID CREATED!")
    print(f"📁 File: {output_file}")
    print(f"📊 Size: {file_size:.2f} MB")
    print(f"📐 Dimensions: {width}x{height}px")
    print("\n📝 Shows all 100 characters in one image!")
    print("   Great for showing the full bundle variety")
    print("="*70)


if __name__ == "__main__":
    print("\n🎬 Choose what to create:")
    print("1. Animated GIF preview (15 seconds, ~20 characters)")
    print("2. Static grid showing all 100 characters")
    print("3. Both!")
    print()
    
    choice = input("Enter choice (1, 2, or 3): ").strip()
    
    if choice == "1":
        create_quick_preview()
    elif choice == "2":
        create_showcase_grid()
    elif choice == "3":
        create_quick_preview()
        create_showcase_grid()
    else:
        print("Creating animated preview by default...")
        create_quick_preview()
