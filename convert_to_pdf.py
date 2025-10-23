"""
Simple PDF Creator for Customer Download Instructions
Converts TXT to formatted PDF with clickable links
"""

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.colors import blue, black
import os
import re

def create_simple_pdf():
    """Create PDF from customer instructions text file"""
    
    input_file = "CUSTOMER_DOWNLOAD_INSTRUCTIONS.txt"
    output_file = "CUSTOMER_DOWNLOAD_INSTRUCTIONS.pdf"
    
    if not os.path.exists(input_file):
        print(f"❌ File not found: {input_file}")
        return
    
    print("\n" + "="*70)
    print("📄 CREATING PDF")
    print("="*70)
    print()
    
    # Read the text file
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # Create PDF
    c = canvas.Canvas(output_file, pagesize=letter)
    width, height = letter
    
    # Starting position
    y = height - 0.75*inch
    x = 0.75*inch
    line_height = 12
    
    print("⏳ Generating PDF...")
    
    for line in lines:
        line = line.rstrip()
        
        # Check if we need a new page
        if y < inch:
            c.showPage()
            y = height - 0.75*inch
        
        # Skip empty separator lines
        if line.strip().startswith('====') or line.strip().startswith('────'):
            y -= line_height * 0.5
            continue
        
        # Empty lines
        if not line.strip():
            y -= line_height * 0.5
            continue
        
        # Main title
        if '🎃 HALLOWEEN CHARACTER BUNDLE' in line:
            c.setFont("Helvetica-Bold", 16)
            c.setFillColorRGB(1, 0.42, 0)  # Orange
            c.drawCentredString(width/2, y, line.strip())
            y -= line_height * 2
            c.setFillColorRGB(0, 0, 0)  # Back to black
            continue
        
        # Section headings (with emojis)
        if any(emoji in line for emoji in ['📥', '⚠️', '❓', '📞', '🎨', '✨', '💡', '🌟']):
            c.setFont("Helvetica-Bold", 12)
            c.setFillColorRGB(0.2, 0.2, 0.2)
            c.drawCentredString(width/2, y, line.strip())
            y -= line_height * 1.5
            c.setFillColorRGB(0, 0, 0)
            continue
        
        # Step headings
        if line.strip().startswith('STEP '):
            c.setFont("Helvetica-Bold", 11)
            c.setFillColorRGB(1, 0.42, 0)  # Orange
            text = line.strip()
            c.drawString(x, y, text[:80])  # Limit length
            y -= line_height * 1.5
            c.setFillColorRGB(0, 0, 0)
            continue
        
        # Problem headings
        if line.strip().startswith('PROBLEM:'):
            c.setFont("Helvetica-Bold", 10)
            c.setFillColorRGB(0.8, 0, 0)  # Red
            c.drawString(x, y, line.strip()[:80])
            y -= line_height * 1.2
            c.setFillColorRGB(0, 0, 0)
            continue
        
        # Solution/Note labels
        if line.strip().startswith(('SOLUTION:', 'NOTE:', 'METHOD')):
            c.setFont("Helvetica-Bold", 10)
            c.drawString(x + 20, y, line.strip()[:75])
            y -= line_height * 1.2
            continue
        
        # Regular text
        if line.strip():
            c.setFont("Helvetica", 9)
            text = line.strip()
            
            # Check if line contains a URL
            url_pattern = r'https?://[^\s]+'
            urls = re.findall(url_pattern, text)
            
            if urls:
                # This line contains a URL - make it blue and clickable
                c.setFillColor(blue)
                c.setFont("Helvetica", 9)
                
                # Handle long lines with URLs - wrap text
                if len(text) > 90:
                    # Split at URL
                    before_url = text.split('http')[0]
                    url = urls[0]
                    after_url = text.split(url)[-1] if url in text else ""
                    
                    # Draw before URL part
                    if before_url:
                        c.drawString(x + 20, y, before_url[:80])
                        y -= line_height
                        if y < inch:
                            c.showPage()
                            y = height - 0.75*inch
                    
                    # Draw URL as clickable link
                    c.setFillColor(blue)
                    c.drawString(x + 20, y, url)
                    c.linkURL(url, (x + 20, y - 2, x + 20 + len(url) * 5, y + 10))
                    y -= line_height
                    
                    # Draw after URL part
                    if after_url.strip():
                        c.setFillColor(black)
                        c.drawString(x + 20, y, after_url.strip()[:80])
                        y -= line_height
                else:
                    # Short line with URL
                    c.setFillColor(blue)
                    c.drawString(x + 20, y, text[:90])
                    # Make the URL clickable
                    for url in urls:
                        c.linkURL(url, (x + 20, y - 2, x + 20 + len(url) * 5, y + 10))
                    y -= line_height
                
                c.setFillColor(black)
                continue
            
            # Handle long lines - wrap text
            if len(text) > 90:
                words = text.split()
                current_line = ""
                for word in words:
                    if len(current_line + word) < 85:
                        current_line += word + " "
                    else:
                        c.drawString(x + 20, y, current_line)
                        y -= line_height
                        if y < inch:
                            c.showPage()
                            y = height - 0.75*inch
                        current_line = word + " "
                if current_line:
                    c.drawString(x + 20, y, current_line)
                    y -= line_height
            else:
                c.drawString(x + 20, y, text)
                y -= line_height
    
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
    print("✅ Your download instructions are now in PDF format!")
    print("📤 Ready to upload to Etsy digital files section")
    print("="*70)


if __name__ == "__main__":
    try:
        create_simple_pdf()
    except Exception as e:
        print(f"\n❌ Error creating PDF: {e}")
        import traceback
        traceback.print_exc()
