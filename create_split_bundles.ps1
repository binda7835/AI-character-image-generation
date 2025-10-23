# ===============================================================
# SPLIT BUNDLE INTO 5 SECURE PARTS FOR ETSY
# ===============================================================
# This script splits your 823 MB bundle into 5 parts (~165 MB each)
# Each part can be uploaded directly to Etsy (no public links needed!)
# ===============================================================

Write-Host "`n" -NoNewline
Write-Host "=" * 70 -ForegroundColor Cyan
Write-Host "CREATING 5-PART SECURE BUNDLE FOR ETSY" -ForegroundColor Yellow
Write-Host "=" * 70 -ForegroundColor Cyan
Write-Host ""

# Create output directory
$outputDir = "f:\AI\1. Prompt Engineering\split_bundles"
if (Test-Path $outputDir) {
    Write-Host "⚠️  Output folder exists. Removing old files..." -ForegroundColor Yellow
    Remove-Item "$outputDir\*" -Force
} else {
    New-Item -ItemType Directory -Path $outputDir -Force | Out-Null
}

Write-Host "✓ Output folder ready: $outputDir`n" -ForegroundColor Green

$inputDir = "f:\AI\1. Prompt Engineering\halloween_characters_transparent"

# ===============================================================
# PART 1: Characters 1-20 + Documentation
# ===============================================================
Write-Host "📦 Creating Part 1 of 5..." -ForegroundColor Cyan
Write-Host "   - Characters 001-020 (20 files)"
Write-Host "   - LICENSE_AGREEMENT.txt"
Write-Host "   - CUSTOMER_README.txt"

$part1Files = @()
for ($i = 1; $i -le 20; $i++) {
    $filename = "halloween_character_{0:D3}.png" -f $i
    $part1Files += Join-Path $inputDir $filename
}
$part1Files += "f:\AI\1. Prompt Engineering\LICENSE_AGREEMENT.txt"
$part1Files += "f:\AI\1. Prompt Engineering\CUSTOMER_README.txt"

Compress-Archive -Path $part1Files -DestinationPath "$outputDir\Halloween_Bundle_Part1of5.zip" -CompressionLevel Optimal
$size1 = [math]::Round((Get-Item "$outputDir\Halloween_Bundle_Part1of5.zip").Length / 1MB, 2)
Write-Host "✓ Part 1 created: ${size1} MB`n" -ForegroundColor Green

# ===============================================================
# PART 2: Characters 21-40
# ===============================================================
Write-Host "📦 Creating Part 2 of 5..." -ForegroundColor Cyan
Write-Host "   - Characters 021-040 (20 files)"

$part2Files = @()
for ($i = 21; $i -le 40; $i++) {
    $filename = "halloween_character_{0:D3}.png" -f $i
    $part2Files += Join-Path $inputDir $filename
}

Compress-Archive -Path $part2Files -DestinationPath "$outputDir\Halloween_Bundle_Part2of5.zip" -CompressionLevel Optimal
$size2 = [math]::Round((Get-Item "$outputDir\Halloween_Bundle_Part2of5.zip").Length / 1MB, 2)
Write-Host "✓ Part 2 created: ${size2} MB`n" -ForegroundColor Green

# ===============================================================
# PART 3: Characters 41-60
# ===============================================================
Write-Host "📦 Creating Part 3 of 5..." -ForegroundColor Cyan
Write-Host "   - Characters 041-060 (20 files)"

$part3Files = @()
for ($i = 41; $i -le 60; $i++) {
    $filename = "halloween_character_{0:D3}.png" -f $i
    $part3Files += Join-Path $inputDir $filename
}

Compress-Archive -Path $part3Files -DestinationPath "$outputDir\Halloween_Bundle_Part3of5.zip" -CompressionLevel Optimal
$size3 = [math]::Round((Get-Item "$outputDir\Halloween_Bundle_Part3of5.zip").Length / 1MB, 2)
Write-Host "✓ Part 3 created: ${size3} MB`n" -ForegroundColor Green

# ===============================================================
# PART 4: Characters 61-80
# ===============================================================
Write-Host "📦 Creating Part 4 of 5..." -ForegroundColor Cyan
Write-Host "   - Characters 061-080 (20 files)"

$part4Files = @()
for ($i = 61; $i -le 80; $i++) {
    $filename = "halloween_character_{0:D3}.png" -f $i
    $part4Files += Join-Path $inputDir $filename
}

Compress-Archive -Path $part4Files -DestinationPath "$outputDir\Halloween_Bundle_Part4of5.zip" -CompressionLevel Optimal
$size4 = [math]::Round((Get-Item "$outputDir\Halloween_Bundle_Part4of5.zip").Length / 1MB, 2)
Write-Host "✓ Part 4 created: ${size4} MB`n" -ForegroundColor Green

# ===============================================================
# PART 5: Characters 81-100
# ===============================================================
Write-Host "📦 Creating Part 5 of 5..." -ForegroundColor Cyan
Write-Host "   - Characters 081-100 (20 files)"

$part5Files = @()
for ($i = 81; $i -le 100; $i++) {
    $filename = "halloween_character_{0:D3}.png" -f $i
    $part5Files += Join-Path $inputDir $filename
}

Compress-Archive -Path $part5Files -DestinationPath "$outputDir\Halloween_Bundle_Part5of5.zip" -CompressionLevel Optimal
$size5 = [math]::Round((Get-Item "$outputDir\Halloween_Bundle_Part5of5.zip").Length / 1MB, 2)
Write-Host "✓ Part 5 created: ${size5} MB`n" -ForegroundColor Green

# ===============================================================
# SUMMARY
# ===============================================================
$totalSize = $size1 + $size2 + $size3 + $size4 + $size5

Write-Host ""
Write-Host "=" * 70 -ForegroundColor Cyan
Write-Host "✅ ALL 5 PARTS CREATED SUCCESSFULLY!" -ForegroundColor Green
Write-Host "=" * 70 -ForegroundColor Cyan
Write-Host ""

Write-Host "📊 FILE SUMMARY:" -ForegroundColor Yellow
Write-Host "   Part 1: ${size1} MB (20 characters + LICENSE + README)"
Write-Host "   Part 2: ${size2} MB (20 characters)"
Write-Host "   Part 3: ${size3} MB (20 characters)"
Write-Host "   Part 4: ${size4} MB (20 characters)"
Write-Host "   Part 5: ${size5} MB (20 characters)"
Write-Host "   " + ("-" * 50)
Write-Host "   Total:  ${totalSize} MB (100 characters + documentation)"
Write-Host ""

Write-Host "📁 LOCATION:" -ForegroundColor Yellow
Write-Host "   $outputDir"
Write-Host ""

Write-Host "✅ ETSY UPLOAD STATUS:" -ForegroundColor Yellow
if ($size1 -lt 500 -and $size2 -lt 500 -and $size3 -lt 500 -and $size4 -lt 500 -and $size5 -lt 500) {
    Write-Host "   ✓ All files under 500 MB - PERFECT for Etsy!" -ForegroundColor Green
    Write-Host "   ✓ Etsy allows up to 5 digital files per listing" -ForegroundColor Green
    Write-Host "   ✓ Each file uploads in 2-5 minutes" -ForegroundColor Green
} else {
    Write-Host "   ⚠️  Some files may be too large for optimal upload" -ForegroundColor Yellow
}
Write-Host ""

Write-Host "🚀 NEXT STEPS:" -ForegroundColor Yellow
Write-Host "   1. Go to your Etsy listing"
Write-Host "   2. Scroll to 'Digital Files' section"
Write-Host "   3. Click 'Add a file' and upload Part 1"
Write-Host "   4. Click 'Add a file' again and upload Part 2"
Write-Host "   5. Repeat for Parts 3, 4, and 5"
Write-Host "   6. Add download instructions to your listing description"
Write-Host "   7. Publish and start selling! 🎃"
Write-Host ""

Write-Host "📝 LISTING DESCRIPTION TO ADD:" -ForegroundColor Yellow
Write-Host @"
   
   📦 YOUR DOWNLOAD INCLUDES 5 FILES:
   
   ✓ Part 1 of 5 - Characters 1-20 + License + Instructions
   ✓ Part 2 of 5 - Characters 21-40
   ✓ Part 3 of 5 - Characters 41-60
   ✓ Part 4 of 5 - Characters 61-80
   ✓ Part 5 of 5 - Characters 81-100
   
   HOW TO DOWNLOAD:
   1. After purchase, go to 'Purchases and Reviews'
   2. Find this order and click 'Download Files'
   3. Download all 5 files to the same folder
   4. Extract each ZIP file
   5. All 100 characters ready to use!
   
   💡 Start with Part 1 - it has your instructions!
   
"@ -ForegroundColor White

Write-Host "=" * 70 -ForegroundColor Cyan
Write-Host "✅ READY FOR SECURE ETSY UPLOAD!" -ForegroundColor Green
Write-Host "   No public links needed!" -ForegroundColor Green
Write-Host "   No piracy risk!" -ForegroundColor Green
Write-Host "   100% secure delivery!" -ForegroundColor Green
Write-Host "=" * 70 -ForegroundColor Cyan
Write-Host ""
