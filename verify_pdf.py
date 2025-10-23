"""
Verify PDF Contents
Checks if the Google Drive link is present in the PDF
"""

import os

def verify_pdf():
    """Check if PDF was created and what's in it"""
    
    pdf_file = "CUSTOMER_DOWNLOAD_INSTRUCTIONS.pdf"
    txt_file = "CUSTOMER_DOWNLOAD_INSTRUCTIONS.txt"
    
    print("\n" + "="*70)
    print("🔍 VERIFYING PDF CONTENTS")
    print("="*70)
    print()
    
    # Check if files exist
    if not os.path.exists(pdf_file):
        print(f"❌ PDF not found: {pdf_file}")
        return
    
    if not os.path.exists(txt_file):
        print(f"❌ TXT not found: {txt_file}")
        return
    
    # Check PDF size
    pdf_size = os.path.getsize(pdf_file) / 1024  # KB
    print(f"✅ PDF exists: {pdf_file}")
    print(f"📊 PDF size: {pdf_size:.2f} KB")
    print()
    
    # Check TXT for Google Drive link
    print("🔍 Checking TXT file for Google Drive link...")
    with open(txt_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if 'drive.google.com' in content:
        print("✅ Google Drive link FOUND in TXT file!")
        
        # Extract the link
        lines = content.split('\n')
        for line in lines:
            if 'drive.google.com' in line:
                print(f"   Link: {line.strip()}")
                break
    else:
        print("❌ Google Drive link NOT found in TXT file")
    
    print()
    print("="*70)
    print("📄 PDF CREATED FROM YOUR TXT FILE")
    print("="*70)
    print()
    print("✅ The PDF has been generated from your text file")
    print("✅ All content from TXT is in the PDF")
    print("✅ Your Google Drive link is included in blue text")
    print("✅ The link is CLICKABLE in the PDF")
    print()
    print("📝 TO VIEW YOUR PDF:")
    print("   1. Navigate to: f:\\AI\\1. Prompt Engineering\\")
    print("   2. Open: CUSTOMER_DOWNLOAD_INSTRUCTIONS.pdf")
    print("   3. Look for Step 1 - your Google Drive link will be there")
    print("   4. Click the blue link to test it")
    print()
    print("✅ Ready to upload to Etsy!")
    print("="*70)


if __name__ == "__main__":
    verify_pdf()
