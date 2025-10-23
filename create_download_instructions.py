"""
Create Professional Download Instructions PDF
For Google Drive delivery method
"""

from PIL import Image, ImageDraw, ImageFont

def create_download_instructions_pdf():
    """Create a professional download instructions image (convert to PDF)"""
    
    # Create image (8.5" x 11" at 150 DPI for reasonable file size)
    width = 1275  # 8.5 inches * 150 DPI
    height = 1650  # 11 inches * 150 DPI
    
    # Create white background
    img = Image.new('RGB', (width, height), 'white')
    draw = ImageDraw.Draw(img)
    
    # Try to load fonts
    try:
        title_font = ImageFont.truetype("arialbd.ttf", 60)
        heading_font = ImageFont.truetype("arialbd.ttf", 40)
        body_font = ImageFont.truetype("arial.ttf", 28)
        small_font = ImageFont.truetype("arial.ttf", 24)
    except:
        title_font = ImageFont.load_default()
        heading_font = title_font
        body_font = title_font
        small_font = title_font
    
    y_pos = 80
    
    # Header with orange background
    draw.rectangle([(0, 0), (width, 150)], fill='#ff6b00')
    draw.text((width//2, 75), "🎃 HALLOWEEN CHARACTER BUNDLE", 
             fill='white', font=title_font, anchor='mm')
    
    y_pos = 200
    
    # Download Instructions
    draw.text((width//2, y_pos), "Download Instructions", 
             fill='#333333', font=heading_font, anchor='mm')
    y_pos += 80
    
    # Thank you message
    draw.text((width//2, y_pos), "Thank you for your purchase!", 
             fill='#666666', font=body_font, anchor='mm')
    y_pos += 100
    
    # Step 1
    draw.rectangle([(100, y_pos-10), (width-100, y_pos+40)], fill='#f5f5f5')
    draw.text((150, y_pos + 15), "STEP 1: Download Your Bundle", 
             fill='#ff6b00', font=heading_font, anchor='lm')
    y_pos += 80
    
    draw.text((150, y_pos), "Click the download link below to get your files:", 
             fill='#333333', font=body_font, anchor='lm')
    y_pos += 60
    
    # Download link box
    draw.rectangle([(120, y_pos-5), (width-120, y_pos+55)], 
                  outline='#ff6b00', width=3)
    draw.text((width//2, y_pos + 25), "[ PASTE YOUR GOOGLE DRIVE LINK HERE ]", 
             fill='#0066cc', font=body_font, anchor='mm')
    y_pos += 100
    
    draw.text((150, y_pos), "File size: 823 MB (large download - please be patient!)", 
             fill='#999999', font=small_font, anchor='lm')
    y_pos += 100
    
    # Step 2
    draw.rectangle([(100, y_pos-10), (width-100, y_pos+40)], fill='#f5f5f5')
    draw.text((150, y_pos + 15), "STEP 2: Extract the ZIP File", 
             fill='#ff6b00', font=heading_font, anchor='lm')
    y_pos += 80
    
    instructions = [
        "• The download is a ZIP file (compressed folder)",
        "• Right-click the file → Select 'Extract All' or 'Unzip'",
        "• Choose where to save the extracted files",
        "• You'll get 100 PNG files + license + guide"
    ]
    
    for instruction in instructions:
        draw.text((150, y_pos), instruction, 
                 fill='#333333', font=body_font, anchor='lm')
        y_pos += 45
    
    y_pos += 60
    
    # Step 3
    draw.rectangle([(100, y_pos-10), (width-100, y_pos+40)], fill='#f5f5f5')
    draw.text((150, y_pos + 15), "STEP 3: Start Creating!", 
             fill='#ff6b00', font=heading_font, anchor='lm')
    y_pos += 80
    
    features = [
        "✓ 100 unique Halloween characters",
        "✓ All with transparent backgrounds",
        "✓ 4500 x 5400 pixels each (15\" x 18\" at 300 DPI)",
        "✓ Commercial license included",
        "✓ Ready for print-on-demand, crafts, and more!"
    ]
    
    for feature in features:
        draw.text((150, y_pos), feature, 
                 fill='#333333', font=body_font, anchor='lm')
        y_pos += 45
    
    y_pos += 80
    
    # Need Help section
    draw.rectangle([(100, y_pos-10), (width-100, y_pos+110)], 
                  fill='#fff5e6', outline='#ff6b00', width=2)
    draw.text((width//2, y_pos + 20), "Need Help?", 
             fill='#ff6b00', font=heading_font, anchor='mm')
    draw.text((width//2, y_pos + 65), "Message us through Etsy anytime!", 
             fill='#333333', font=body_font, anchor='mm')
    
    # Footer
    draw.text((width//2, height - 60), "Happy Creating! 👻🦇🎃", 
             fill='#999999', font=body_font, anchor='mm')
    
    # Save as PNG first
    output_png = "Download_Instructions.png"
    img.save(output_png, 'PNG', dpi=(150, 150))
    
    print("\n" + "="*70)
    print("✅ DOWNLOAD INSTRUCTIONS IMAGE CREATED!")
    print("="*70)
    print(f"📄 File: {output_png}")
    print()
    print("📝 NEXT STEPS:")
    print("="*70)
    print()
    print("1. UPLOAD YOUR ZIP TO GOOGLE DRIVE:")
    print("   - Go to drive.google.com")
    print("   - Click 'New' → 'File upload'")
    print("   - Select: Halloween_Character_Bundle.zip")
    print("   - Wait for upload (5-10 minutes)")
    print()
    print("2. GET SHAREABLE LINK:")
    print("   - Right-click the uploaded file")
    print("   - Click 'Get link'")
    print("   - Change to: 'Anyone with the link can view'")
    print("   - Copy the link")
    print()
    print("3. EDIT THE DOWNLOAD INSTRUCTIONS:")
    print("   - Open this image in any image editor")
    print("   - Replace '[ PASTE YOUR GOOGLE DRIVE LINK HERE ]'")
    print("   - With your actual Google Drive link")
    print("   - Save as PDF")
    print()
    print("4. UPLOAD TO ETSY:")
    print("   - In your Etsy listing")
    print("   - Digital Files section")
    print("   - Upload the edited PDF")
    print("   - Done! (PDF is only ~1 MB)")
    print()
    print("="*70)
    print("💡 TIP: You can also create a PDF with this link using:")
    print("   - Microsoft Word")
    print("   - Google Docs")
    print("   - Canva (free)")
    print("   - Any PDF creator")
    print("="*70)


if __name__ == "__main__":
    create_download_instructions_pdf()
