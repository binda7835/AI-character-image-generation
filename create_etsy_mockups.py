"""
Etsy Mockup Generator
Creates 20 professional mockup images for Etsy listing
Shows Halloween characters on various products and in use
"""

import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random

class EtsyMockupGenerator:
    def __init__(self):
        self.input_dir = "halloween_characters_transparent"
        self.output_dir = "etsy_mockups"
        self.mockup_width = 2000
        self.mockup_height = 2200  # Increased height to fit all rows
        
        os.makedirs(self.output_dir, exist_ok=True)
    
    def create_bundle_showcase(self, image_numbers, output_name, title):
        """Create a grid showcase of multiple characters"""
        grid_size = 4  # 4x4 grid
        title_height = 250  # Increased title space
        grid_height = self.mockup_height - title_height
        cell_size = grid_height // grid_size  # Calculate based on available space
        
        # Create white background
        mockup = Image.new('RGB', (self.mockup_width, self.mockup_height), 'white')
        draw = ImageDraw.Draw(mockup)
        
        # Add title at top
        try:
            font = ImageFont.truetype("arial.ttf", 80)
            title_font = ImageFont.truetype("arialbd.ttf", 100)
        except:
            font = ImageFont.load_default()
            title_font = font
        
        # Title background
        draw.rectangle([(0, 0), (self.mockup_width, title_height)], fill='#ff6b00')
        draw.text((self.mockup_width//2, title_height//2), title, fill='white', 
                 font=title_font, anchor='mm')
        
        # Place characters in grid
        for i, img_num in enumerate(image_numbers[:16]):  # Max 16 for 4x4
            row = i // grid_size
            col = i % grid_size
            
            x = col * cell_size
            y = row * cell_size + title_height  # Offset for title
            
            # Load character
            img_path = os.path.join(self.input_dir, f"halloween_character_{img_num:03d}.png")
            if os.path.exists(img_path):
                try:
                    with Image.open(img_path) as char_img:
                        # Resize more efficiently - ensure it fits in cell
                        padding = 30
                        max_size = cell_size - padding
                        char_img.thumbnail((max_size, max_size), Image.Resampling.LANCZOS)
                        
                        # Center in cell
                        x_offset = x + (cell_size - char_img.width) // 2
                        y_offset = y + (cell_size - char_img.height) // 2
                        
                        # Paste on mockup
                        mockup.paste(char_img, (x_offset, y_offset), char_img if char_img.mode == 'RGBA' else None)
                except Exception as e:
                    print(f"⚠️  Error loading character {img_num}: {e}")
        
        # Save
        output_path = os.path.join(self.output_dir, output_name)
        mockup.save(output_path, 'PNG', dpi=(300, 300))
        print(f"✓ Created: {output_name}")
    
    def create_tshirt_mockup(self, char_num, output_name):
        """Create t-shirt product mockup"""
        # Create t-shirt background
        mockup = Image.new('RGB', (self.mockup_width, self.mockup_height), '#f5f5f5')
        draw = ImageDraw.Draw(mockup)
        
        # Draw t-shirt shape
        tshirt_color = random.choice(['#000000', '#ffffff', '#ff6b00', '#8b00ff'])
        
        # Simple t-shirt rectangle
        tshirt_x = 400
        tshirt_y = 300
        tshirt_w = 1200
        tshirt_h = 1200
        
        draw.rectangle([(tshirt_x, tshirt_y), (tshirt_x+tshirt_w, tshirt_y+tshirt_h)], 
                      fill=tshirt_color)
        
        # Load and place character
        img_path = os.path.join(self.input_dir, f"halloween_character_{char_num:03d}.png")
        if os.path.exists(img_path):
            try:
                with Image.open(img_path) as char_img:
                    char_img.thumbnail((600, 600), Image.Resampling.LANCZOS)
                    
                    # Center on t-shirt
                    char_x = tshirt_x + (tshirt_w - char_img.width) // 2
                    char_y = tshirt_y + (tshirt_h - char_img.height) // 2
                    
                    mockup.paste(char_img, (char_x, char_y), char_img if char_img.mode == 'RGBA' else None)
            except Exception as e:
                print(f"⚠️  Error loading character {char_num}: {e}")
        
        # Add text
        try:
            font = ImageFont.truetype("arial.ttf", 60)
        except:
            font = ImageFont.load_default()
        
        draw.text((self.mockup_width//2, 150), "Print-Ready Design", 
                 fill='#333333', font=font, anchor='mm')
        
        output_path = os.path.join(self.output_dir, output_name)
        mockup.save(output_path, 'PNG', dpi=(300, 300))
        print(f"✓ Created: {output_name}")
    
    def create_mug_mockup(self, char_num, output_name):
        """Create mug product mockup"""
        mockup = Image.new('RGB', (self.mockup_width, self.mockup_height), '#ffffff')
        draw = ImageDraw.Draw(mockup)
        
        # Draw mug shape (simplified cylinder)
        mug_x = 600
        mug_y = 500
        mug_w = 800
        mug_h = 1000
        
        # Mug body
        draw.rectangle([(mug_x, mug_y), (mug_x+mug_w, mug_y+mug_h)], 
                      fill='#ffffff', outline='#333333', width=5)
        
        # Load character
        img_path = os.path.join(self.input_dir, f"halloween_character_{char_num:03d}.png")
        if os.path.exists(img_path):
            try:
                with Image.open(img_path) as char_img:
                    char_img.thumbnail((500, 500), Image.Resampling.LANCZOS)
                    
                    char_x = mug_x + (mug_w - char_img.width) // 2
                    char_y = mug_y + (mug_h - char_img.height) // 2
                    
                    mockup.paste(char_img, (char_x, char_y), char_img if char_img.mode == 'RGBA' else None)
            except Exception as e:
                print(f"⚠️  Error loading character {char_num}: {e}")
        
        output_path = os.path.join(self.output_dir, output_name)
        mockup.save(output_path, 'PNG', dpi=(300, 300))
        print(f"✓ Created: {output_name}")
    
    def create_specifications_image(self):
        """Create an image showing product specifications"""
        mockup = Image.new('RGB', (self.mockup_width, self.mockup_height), '#2d2d2d')
        draw = ImageDraw.Draw(mockup)
        
        try:
            title_font = ImageFont.truetype("arialbd.ttf", 120)
            font = ImageFont.truetype("arial.ttf", 70)
        except:
            title_font = ImageFont.load_default()
            font = title_font
        
        # Title
        draw.text((self.mockup_width//2, 200), "BUNDLE INCLUDES", 
                 fill='#ff6b00', font=title_font, anchor='mm')
        
        # Specifications
        specs = [
            "✓ 100 Unique Characters",
            "✓ PNG Format",
            "✓ Transparent Background",
            "✓ 4500 x 5400 Pixels",
            "✓ 300 DPI Quality",
            "✓ Commercial License",
            "✓ Instant Download"
        ]
        
        y_pos = 400
        for spec in specs:
            draw.text((self.mockup_width//2, y_pos), spec, 
                     fill='white', font=font, anchor='mm')
            y_pos += 150
        
        output_path = os.path.join(self.output_dir, "mockup_01_specifications.png")
        mockup.save(output_path, 'PNG', dpi=(300, 300))
        print(f"✓ Created: mockup_01_specifications.png")
    
    def generate_all_mockups(self):
        """Generate all 20 mockup images"""
        print("\n" + "="*70)
        print("🎨 GENERATING ETSY MOCKUPS")
        print("="*70)
        print()
        
        # Mockup 1: Specifications
        self.create_specifications_image()
        
        # Mockup 2-5: Character showcases (different categories)
        self.create_bundle_showcase([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16], 
                                   "mockup_02_vampires_witches.png", 
                                   "Vampires & Witches")
        
        self.create_bundle_showcase([17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32], 
                                   "mockup_03_zombies_ghosts.png", 
                                   "Zombies & Ghosts")
        
        self.create_bundle_showcase([33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48], 
                                   "mockup_04_monsters_creatures.png", 
                                   "Monsters & Creatures")
        
        self.create_bundle_showcase([49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64], 
                                   "mockup_05_demons_spirits.png", 
                                   "Demons & Spirits")
        
        # Mockup 6-10: T-shirt mockups
        for i, char_num in enumerate([5, 15, 25, 35, 45], start=6):
            self.create_tshirt_mockup(char_num, f"mockup_{i:02d}_tshirt_{i-5}.png")
        
        # Mockup 11-15: Mug mockups
        for i, char_num in enumerate([10, 20, 30, 40, 50], start=11):
            self.create_mug_mockup(char_num, f"mockup_{i:02d}_mug_{i-10}.png")
        
        # Mockup 16-20: More showcases
        self.create_bundle_showcase([65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80], 
                                   "mockup_16_collection_1.png", 
                                   "Collection Part 1")
        
        self.create_bundle_showcase([81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96], 
                                   "mockup_17_collection_2.png", 
                                   "Collection Part 2")
        
        self.create_bundle_showcase([1,12,23,34,45,56,67,78,89,100,11,22,33,44,55,66], 
                                   "mockup_18_variety_mix.png", 
                                   "Variety Showcase")
        
        self.create_bundle_showcase([5,15,25,35,45,55,65,75,85,95,10,20,30,40,50,60], 
                                   "mockup_19_best_sellers.png", 
                                   "Featured Characters")
        
        # Final mockup: Call to action
        mockup = Image.new('RGB', (self.mockup_width, self.mockup_height), '#8b00ff')
        draw = ImageDraw.Draw(mockup)
        
        try:
            big_font = ImageFont.truetype("arialbd.ttf", 140)
            med_font = ImageFont.truetype("arial.ttf", 80)
        except:
            big_font = ImageFont.load_default()
            med_font = big_font
        
        draw.text((self.mockup_width//2, 700), "100 CHARACTERS", 
                 fill='white', font=big_font, anchor='mm')
        draw.text((self.mockup_width//2, 900), "Instant Download", 
                 fill='#ff6b00', font=med_font, anchor='mm')
        draw.text((self.mockup_width//2, 1100), "Commercial License", 
                 fill='#ff6b00', font=med_font, anchor='mm')
        draw.text((self.mockup_width//2, 1300), "300 DPI Quality", 
                 fill='#ff6b00', font=med_font, anchor='mm')
        
        output_path = os.path.join(self.output_dir, "mockup_20_call_to_action.png")
        mockup.save(output_path, 'PNG', dpi=(300, 300))
        print(f"✓ Created: mockup_20_call_to_action.png")
        
        print("\n" + "="*70)
        print("✅ ALL 20 MOCKUPS CREATED!")
        print(f"📁 Location: {self.output_dir}/")
        print("="*70)


if __name__ == "__main__":
    generator = EtsyMockupGenerator()
    generator.generate_all_mockups()
