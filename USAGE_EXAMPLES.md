# 🎯 CodeCrafter Usage Examples

This document provides comprehensive examples of how to use CodeCrafter in different scenarios.

## 🚀 Multiple Ways to Run CodeCrafter

### Method 1: Standalone Script (Recommended)
```bash
python CodeCrafter.py --version
python CodeCrafter.py --encode base64 --input "Hello World"
```

### Method 2: Windows Batch File
```cmd
CodeCrafter.bat --version
CodeCrafter.bat --encode url --input "hello world"
```

### Method 3: Python Module
```bash
python -m codecrafter --version
python -m codecrafter --encode html --input "<test>"
```

### Method 4: System Installation (After pip install)
```bash
codecrafter --version
codecrafter --encode rot13 --input "Hello"
```

## 📝 Complete Command Examples

### Base64 Operations
```bash
# Encode
python CodeCrafter.py --encode base64 --input "Hello World"
# Output: BASE64 Encode: SGVsbG8gV29ybGQ=

# Decode  
codecrafter --decode base64 --input "SGVsbG8gV29ybGQ="
# Output: BASE64 Decode: Hello World
```

### URL Operations
```bash
# Encode
CodeCrafter.bat --encode url --input "hello world & symbols"
# Output: URL Encode: hello%20world%20%26%20symbols

# Decode
python CodeCrafter.py --decode url --input "hello%20world%20%26%20symbols"
# Output: URL Decode: hello world & symbols
```

### HTML Entity Operations
```bash
# Encode
codecrafter --encode html --input "<script>alert('XSS')</script>"
# Output: HTML Encode: &lt;script&gt;alert(&#x27;XSS&#x27;)&lt;/script&gt;

# Decode
python CodeCrafter.py --decode html --input "&lt;test&gt;"
# Output: HTML Decode: <test>
```

### ROT Ciphers
```bash
# ROT13
CodeCrafter.bat --encode rot13 --input "Hello World"
# Output: ROT13: Uryyb Jbeyq

# ROT47
codecrafter --encode rot47 --input "Hello 123!"
# Output: ROT47: w6==@ `abd
```

### Binary & Hex Conversions
```bash
# Binary to Hex
python CodeCrafter.py --convert bin-to-hex --input "1010"
# Output: Bin To Hex: A

# Binary to Decimal
CodeCrafter.bat --convert bin-to-decimal --input "1010"
# Output: Bin To Decimal: 10

# Hex to String
codecrafter --convert hex-to-string --input "48656c6c6f"
# Output: Hex To String: Hello
```

## 📁 File Processing Examples

### Basic File Operations
```bash
# Create test file
echo "Hello from file" > input.txt

# Encode file to Base64
python CodeCrafter.py --encode base64 --file input.txt --output encoded.txt

# Decode back to original
codecrafter --decode base64 --file encoded.txt --output decoded.txt

# Verify result
cat decoded.txt
# Output: Hello from file
```

### Batch Processing Multiple Files
```bash
# Linux/macOS
for file in *.txt; do
    codecrafter --encode base64 --file "$file" --output "${file}.b64"
done

# Windows PowerShell
Get-ChildItem *.txt | ForEach-Object {
    python CodeCrafter.py --encode base64 --file $_.Name --output "$($_.BaseName).b64"
}
```

### Large File Processing
```bash
# Process large files efficiently
codecrafter --encode url --file large_data.txt --output url_encoded.txt
codecrafter --decode html --file web_content.html --output clean_content.txt
```

## 🎮 Interactive Mode Examples

### Starting Interactive Mode
```bash
# Any of these starts interactive mode
python CodeCrafter.py
# or
CodeCrafter.bat
# or
codecrafter
```

### Interactive Session Example
```
Welcome to CodeCrafter v1.0.0!
Created by @Amanja

Select an operation:
 1. Base64 Encode
 2. Base64 Decode
 3. ROT13
 4. ROT47
 5. Hex to String
 6. Binary to Hex
 7. Binary to Decimal
 8. URL Encode
 9. URL Decode
10. HTML Entity Encode
11. HTML Entity Decode
12. Change Banner
 0. Exit

Choice > 1
Enter text to encode (Base64): Hello Interactive Mode
Encoded: SGVsbG8gSW50ZXJhY3RpdmUgTW9kZQ==
```

## 🔗 Chaining Operations (Advanced)

### Using Shell Pipes (Linux/macOS)
```bash
# Encode then decode to verify
echo "Test data" | python CodeCrafter.py --encode base64 --input "$(cat)" | python CodeCrafter.py --decode base64 --input "$(cat)"

# Complex processing pipeline
cat data.txt | \
  codecrafter --encode url --input "$(cat)" | \
  codecrafter --encode base64 --input "$(cat)" > double_encoded.txt
```

### Using Variables
```bash
# Store intermediate results
ENCODED=$(python CodeCrafter.py --encode base64 --input "Hello World")
echo "Encoded: $ENCODED"

DECODED=$(codecrafter --decode base64 --input "$ENCODED")
echo "Decoded: $DECODED"
```

## 🛠️ Development & Testing Examples

### Testing All Operations
```bash
# Test all encoding operations
python CodeCrafter.py --encode base64 --input "test"
python CodeCrafter.py --encode rot13 --input "test"
python CodeCrafter.py --encode rot47 --input "test"
python CodeCrafter.py --encode url --input "test data"
python CodeCrafter.py --encode html --input "<test>"

# Test all conversions
python CodeCrafter.py --convert bin-to-hex --input "1111"
python CodeCrafter.py --convert bin-to-decimal --input "1111"
python CodeCrafter.py --convert hex-to-string --input "74657374"
```

### Validation Testing
```bash
# Test input validation (these should fail gracefully)
python CodeCrafter.py --encode base64 --input ""
python CodeCrafter.py --encode base64 --input "$(python -c 'print("A"*20000)')"

# Test error handling
python CodeCrafter.py --decode base64 --input "invalid-base64"
python CodeCrafter.py --convert hex-to-string --input "invalid-hex"
```

## 🌐 Real-World Use Cases

### Web Development
```bash
# URL encode form data
codecrafter --encode url --input "user@example.com"
codecrafter --encode url --input "search query with spaces"

# HTML escape user input
codecrafter --encode html --input "<script>alert('xss')</script>"
codecrafter --encode html --input "Price: $100 & free shipping"
```

### Security & CTF
```bash
# Decode common CTF encodings
codecrafter --decode base64 --input "Y3RmY3RmY3Rm"
codecrafter --decode hex --input "6374666374666374"
codecrafter --encode rot13 --input "encrypted_flag"

# Chain multiple decodings
STEP1=$(codecrafter --decode base64 --input "SGVsbG8=")
codecrafter --decode hex --input "$STEP1"
```

### Data Processing
```bash
# Clean HTML entities from scraped data
codecrafter --decode html --file scraped_data.html --output clean_data.txt

# Convert binary log files
codecrafter --convert bin-to-hex --file binary_log.txt --output hex_log.txt

# URL decode log files
codecrafter --decode url --file access_log.txt --output decoded_log.txt
```

### API Integration
```bash
# Prepare data for API calls
API_DATA=$(codecrafter --encode url --input "complex data & symbols")
curl -d "$API_DATA" "https://api.example.com/endpoint"

# Decode API responses
codecrafter --decode base64 --input "$API_RESPONSE" > response_data.txt
```

## 🎨 Creative Examples

### Text Art Processing
```bash
# ROT13 text art
codecrafter --encode rot13 --input "ASCII ART TEXT"

# Base64 "hidden" messages
codecrafter --encode base64 --input "Secret message in Base64"
```

### Educational Examples
```bash
# Demonstrate encoding concepts
echo "Understanding Base64:"
codecrafter --encode base64 --input "Man"
echo "Expected: TWFu"

echo "Understanding URL encoding:"
codecrafter --encode url --input "hello world"
echo "Spaces become %20"
```

## 🔧 System Administration

### Log Processing
```bash
# Process URL-encoded logs
find /var/log -name "*.log" -exec codecrafter --decode url --file {} --output {}.decoded \;

# Convert hex dumps
codecrafter --convert hex-to-string --file hexdump.txt --output readable.txt
```

### Configuration Management
```bash
# Encode sensitive config values
SECRET=$(codecrafter --encode base64 --input "database_password")
echo "DB_PASS_ENCODED=$SECRET" >> .env

# Decode when needed
codecrafter --decode base64 --input "$SECRET"
```

## 💡 Tips & Tricks

### Performance Tips
```bash
# For large files, always use --file instead of --input
codecrafter --encode base64 --file large_file.txt --output encoded.txt

# Use output files for large results
codecrafter --decode html --file big_html.txt --output clean.txt
```

### Scripting Tips
```bash
# Check if encoding succeeded
if codecrafter --encode base64 --input "test" > /dev/null; then
    echo "Encoding works"
fi

# Function for repeated encoding
encode_file() {
    codecrafter --encode base64 --file "$1" --output "$1.b64"
}
```

### Debugging Tips
```bash
# Show help when unsure
python CodeCrafter.py --help

# Test with known values
codecrafter --encode base64 --input "Hello"
# Should output: SGVsbG8=

# Verify round-trip encoding
ORIGINAL="Test Data"
ENCODED=$(codecrafter --encode base64 --input "$ORIGINAL")
DECODED=$(codecrafter --decode base64 --input "$ENCODED")
echo "Original: $ORIGINAL"
echo "Encoded: $ENCODED" 
echo "Decoded: $DECODED"
echo "Match: $([ "$ORIGINAL" = "$DECODED" ] && echo "YES" || echo "NO")"
```

---

**Happy Encoding with CodeCrafter! 🔧✨** 