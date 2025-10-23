"""
Simple PDF with Google Drive Link - GUARANTEED TO SHOW
Creates a clean, simple PDF with the download link prominently displayed
"""

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor
import os

def create_pdf_with_link():
    """Create simple PDF with prominent Google Drive link"""
    
    output_file = "CUSTOMER_DOWNLOAD_INSTRUCTIONS.pdf"
    
    # Your Google Drive link
    GOOGLE_DRIVE_LINK = "https://drive.google.com/file/d/18qISkGJU-4vq39vNVQtyaTbLDvHGPdic/view?usp=drive_link"
    
    print("\n" + "="*70)
    print("📄 CREATING SIMPLE PDF WITH YOUR LINK")
    print("="*70)
    
    # Create PDF
    c = canvas.Canvas(output_file, pagesize=letter)
    width, height = letter
    
    # Colors
    orange = HexColor('#FF6600')
    blue = HexColor('#0066CC')
    black = HexColor('#000000')
    gray = HexColor('#666666')
    
    # Starting position
    y = height - inch
    
    # ============================================================================
    # TITLE
    # ============================================================================
    c.setFillColor(orange)
    c.setFont("Helvetica-Bold", 20)
    c.drawCentredString(width/2, y, "HALLOWEEN CHARACTER BUNDLE")
    y -= 30
    
    c.setFillColor(black)
    c.setFont("Helvetica", 12)
    c.drawCentredString(width/2, y, "100 High-Quality Transparent PNG Characters")
    y -= 60
    
    # ============================================================================
    # MAIN DOWNLOAD SECTION - SUPER PROMINENT
    # ============================================================================
    c.setFillColor(orange)
    c.setFont("Helvetica-Bold", 16)
    c.drawCentredString(width/2, y, "YOUR DOWNLOAD LINK")
    y -= 40
    
    # Draw box around link
    box_height = 60
    box_width = 500
    box_x = (width - box_width) / 2
    box_y = y - box_height + 10
    
    c.setStrokeColor(blue)
    c.setLineWidth(2)
    c.rect(box_x, box_y, box_width, box_height, stroke=1, fill=0)
    
    # Draw the link LARGE and CENTERED
    c.setFillColor(blue)
    c.setFont("Helvetica-Bold", 11)
    link_y = y - 25
    c.drawCentredString(width/2, link_y, GOOGLE_DRIVE_LINK)
    
    # Make it clickable
    link_width = len(GOOGLE_DRIVE_LINK) * 6.5
    link_rect = (
        width/2 - link_width/2,
        link_y - 3,
        width/2 + link_width/2,
        link_y + 12
    )
    c.linkURL(GOOGLE_DRIVE_LINK, link_rect)
    
    y -= 80
    
    c.setFillColor(black)
    c.setFont("Helvetica-Bold", 10)
    c.drawCentredString(width/2, y, "Click the blue link above or copy-paste it into your browser")
    y -= 60
    
    # ============================================================================
    # INSTRUCTIONS
    # ============================================================================
    c.setFillColor(orange)
    c.setFont("Helvetica-Bold", 14)
    c.drawString(inch, y, "STEP 1: Download from Google Drive")
    y -= 25
    
    c.setFillColor(black)
    c.setFont("Helvetica", 10)
    instructions = [
        "1. Click the blue link above (it will open Google Drive in your browser)",
        "2. Click the 'Download' button (top-right corner of Google Drive page)",
        "3. The file is 824 MB - download may take 5-15 minutes depending on your internet speed",
        "4. Save the ZIP file: Halloween_Character_Bundle.zip"
    ]
    
    for instruction in instructions:
        c.drawString(inch + 20, y, instruction)
        y -= 20
    
    y -= 20
    
    # ============================================================================
    c.setFillColor(orange)
    c.setFont("Helvetica-Bold", 14)
    c.drawString(inch, y, "STEP 2: Extract the ZIP File")
    y -= 25
    
    c.setFillColor(black)
    c.setFont("Helvetica", 10)
    extract_steps = [
        "1. Locate the downloaded ZIP file (usually in your Downloads folder)",
        "2. Right-click on 'Halloween_Character_Bundle.zip'",
        "3. Select 'Extract All...' or 'Extract Here'",
        "4. You'll get a folder with 100 transparent PNG files!"
    ]
    
    for step in extract_steps:
        c.drawString(inch + 20, y, step)
        y -= 20
    
    y -= 20
    
    # ============================================================================
    c.setFillColor(orange)
    c.setFont("Helvetica-Bold", 14)
    c.drawString(inch, y, "STEP 3: Start Creating!")
    y -= 25
    
    c.setFillColor(black)
    c.setFont("Helvetica", 10)
    usage_tips = [
        "Each character is 4500x5400 pixels at 300 DPI - perfect for printing!",
        "All backgrounds are transparent - ready to use in any design",
        "Use them for t-shirts, mugs, stickers, posters, digital art, and more!",
        "Commercial use allowed - create and sell unlimited products!"
    ]
    
    for tip in usage_tips:
        c.drawString(inch + 20, y, tip)
        y -= 20
    
    y -= 30
    
    # ============================================================================
    # TROUBLESHOOTING
    # ============================================================================
    c.setFillColor(orange)
    c.setFont("Helvetica-Bold", 12)
    c.drawString(inch, y, "TROUBLESHOOTING")
    y -= 25
    
    c.setFillColor(gray)
    c.setFont("Helvetica-Bold", 10)
    c.drawString(inch + 20, y, "Problem: Link won't open")
    y -= 18
    c.setFillColor(black)
    c.setFont("Helvetica", 9)
    c.drawString(inch + 40, y, "Solution: Copy the link and paste it directly into your browser's address bar")
    y -= 20
    
    c.setFillColor(gray)
    c.setFont("Helvetica-Bold", 10)
    c.drawString(inch + 20, y, "Problem: Download is slow")
    y -= 18
    c.setFillColor(black)
    c.setFont("Helvetica", 9)
    c.drawString(inch + 40, y, "Solution: The file is large (824 MB). Be patient - it may take 10-15 minutes")
    y -= 20
    
    c.setFillColor(gray)
    c.setFont("Helvetica-Bold", 10)
    c.drawString(inch + 20, y, "Problem: Can't extract ZIP file")
    y -= 18
    c.setFillColor(black)
    c.setFont("Helvetica", 9)
    c.drawString(inch + 40, y, "Solution: Windows: right-click > Extract All. Mac: double-click the ZIP file")
    y -= 30
    
    # ============================================================================
    # FOOTER
    # ============================================================================
    c.setFillColor(orange)
    c.setFont("Helvetica-Bold", 10)
    c.drawCentredString(width/2, y, "Need Help? Contact your Etsy seller via Messages")
    y -= 20
    
    c.setFillColor(black)
    c.setFont("Helvetica", 9)
    c.drawCentredString(width/2, y, "Thank you for your purchase! Enjoy creating amazing Halloween designs!")
    
    # ============================================================================
    # PAGE 2 - LICENSE INFORMATION
    # ============================================================================
    c.showPage()
    y = height - inch
    
    c.setFillColor(orange)
    c.setFont("Helvetica-Bold", 16)
    c.drawCentredString(width/2, y, "LICENSE & USAGE RIGHTS")
    y -= 40
    
    c.setFillColor(black)
    c.setFont("Helvetica-Bold", 11)
    c.drawString(inch, y, "WHAT YOU CAN DO:")
    y -= 22
    
    c.setFont("Helvetica", 10)
    allowed_uses = [
        "✓ Use for personal projects (cards, decorations, gifts)",
        "✓ Use for commercial projects (sell products you create)",
        "✓ Print on physical products (t-shirts, mugs, posters, stickers)",
        "✓ Use in digital designs (websites, social media, marketing)",
        "✓ Modify and edit the images as needed",
        "✓ Create unlimited products for sale"
    ]
    
    for use in allowed_uses:
        c.drawString(inch + 20, y, use)
        y -= 20
    
    y -= 20
    
    c.setFont("Helvetica-Bold", 11)
    c.drawString(inch, y, "WHAT YOU CANNOT DO:")
    y -= 22
    
    c.setFont("Helvetica", 10)
    not_allowed = [
        "✗ Resell or redistribute the original PNG files",
        "✗ Share the download link with others",
        "✗ Claim the designs as your own creation",
        "✗ Use in trademarked logos without modification"
    ]
    
    for restriction in not_allowed:
        c.drawString(inch + 20, y, restriction)
        y -= 20
    
    y -= 30
    
    c.setFillColor(orange)
    c.setFont("Helvetica-Bold", 12)
    c.drawCentredString(width/2, y, "Happy Creating!")
    
    # Save PDF
    c.save()
    
    # Get file size
    file_size = os.path.getsize(output_file) / 1024  # KB
    
    print("\n" + "="*70)
    print("✅ PDF CREATED SUCCESSFULLY!")
    print("="*70)
    print(f"📁 File: {output_file}")
    print(f"📊 Size: {file_size:.2f} KB")
    print()
    print(f"🔗 Link included: {GOOGLE_DRIVE_LINK}")
    print()
    print("✅ The link is:")
    print("   • LARGE and centered in a blue box")
    print("   • BLUE colored text")
    print("   • CLICKABLE (try it!)")
    print("   • On the first page")
    print()
    print("📤 Ready to upload to Etsy!")
    print("="*70)


if __name__ == "__main__":
    try:
        create_pdf_with_link()
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
