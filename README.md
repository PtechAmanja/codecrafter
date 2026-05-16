# CodeCrafter

**CodeCrafter** is a lightweight, Python-based encoding and decoding toolkit designed for developers, security researchers, and CTF enthusiasts. Whether you're handling data transformations, exploring steganography, or solving challenges, CodeCrafter provides a comprehensive suite of encoding utilities.

![Python](https://img.shields.io/badge/python-3.6+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey.svg)

## Features

### Encoding & Decoding Operations
- **Base64**: Encode/decode text to/from Base64 format
- **ROT13**: Classic Caesar cipher with 13-character shift
- **ROT47**: Extended ROT cipher for printable ASCII characters
- **URL Encoding**: Percent encoding for safe URL usage
- **HTML Entities**: Convert special characters to HTML entities
- **Hexadecimal**: Convert hex strings to readable text
- **Binary**: Convert binary to hexadecimal and decimal

### Interface Options
- **Interactive CLI**: Beautiful, colorized menu-driven interface
- **Command-line**: Direct operations via command-line arguments
- **File Processing**: Batch processing of files
- **Cross-platform**: Works on Windows, Linux, and macOS

### Security & Quality
- **Input Validation**: Prevents oversized inputs and injection attacks
- **Safe Execution**: Uses `subprocess` instead of `os.system()`
- **Error Handling**: Robust error handling with user-friendly messages
- **No Dependencies**: Uses only Python standard library

## Installation

### Prerequisites
- Python 3.6 or higher
- No external dependencies required

### Quick Install
```bash
# Clone the repository
git clone https://github.com/PtechAmanja/codecrafter.git
cd codecrafter

# Run directly (multiple ways)
python CodeCrafter.py --version
# or
CodeCrafter.bat --version    # Windows
# or
python -m codecrafter --version
```

### Installation Options
1. **Direct execution**: `python CodeCrafter.py`
2. **Windows batch file**: `CodeCrafter.bat`
3. **Python module**: `python -m codecrafter`
4. **System installation**: `pip install -e .` then `codecrafter`

See [INSTALL.md](INSTALL.md) for detailed installation instructions.

## Usage

### Interactive Mode (Default)
```bash
# Any of these will start interactive mode:
python CodeCrafter.py
# or
CodeCrafter.bat           # Windows
# or
codecrafter              # If installed system-wide
```
This launches the colorful, menu-driven interface where you can select operations and input data interactively.

### Command-Line Mode

#### Basic Encoding
```bash
# Base64 encode
python CodeCrafter.py --encode base64 --input "Hello World"
# or
codecrafter --encode base64 --input "Hello World"

# URL encode
CodeCrafter.bat --encode url --input "hello world & more"

# HTML entity encode
python CodeCrafter.py --encode html --input "<script>alert('test')</script>"
```

#### Basic Decoding
```bash
# Base64 decode
codecrafter --decode base64 --input "SGVsbG8gV29ybGQ="

# URL decode
python CodeCrafter.py --decode url --input "hello%20world%20%26%20more"

# HTML entity decode
CodeCrafter.bat --decode html --input "&lt;script&gt;alert(&#x27;test&#x27;)&lt;/script&gt;"
```

#### Conversions
```bash
# Binary to hex
codecrafter --convert bin-to-hex --input "1010"

# Binary to decimal
python CodeCrafter.py --convert bin-to-decimal --input "1010"

# Hex to string
CodeCrafter.bat --convert hex-to-string --input "48656c6c6f"
```

#### File Processing
```bash
# Encode file contents
codecrafter --encode base64 --file input.txt --output encoded.txt

# Decode file contents
python CodeCrafter.py --decode base64 --file encoded.txt --output decoded.txt
```

## API Reference

### Available Operations

| Operation | CLI Flag | Description | Example Input | Example Output |
|-----------|----------|-------------|---------------|----------------|
| Base64 Encode | `--encode base64` | Convert text to Base64 | `Hello` | `SGVsbG8=` |
| Base64 Decode | `--decode base64` | Convert Base64 to text | `SGVsbG8=` | `Hello` |
| ROT13 | `--encode rot13` | Apply ROT13 cipher | `Hello` | `Uryyb` |
| ROT47 | `--encode rot47` | Apply ROT47 cipher | `Hello` | `w6==@` |
| URL Encode | `--encode url` | Percent encode for URLs | `hello world` | `hello%20world` |
| URL Decode | `--decode url` | Decode percent encoding | `hello%20world` | `hello world` |
| HTML Encode | `--encode html` | Convert to HTML entities | `<tag>` | `&lt;tag&gt;` |
| HTML Decode | `--decode html` | Convert HTML entities | `&lt;tag&gt;` | `<tag>` |
| Binary to Hex | `--convert bin-to-hex` | Convert binary to hex | `1010` | `A` |
| Binary to Decimal | `--convert bin-to-decimal` | Convert binary to decimal | `1010` | `10` |
| Hex to String | `--convert hex-to-string` | Convert hex to ASCII | `48656c6c6f` | `Hello` |

### Command-Line Arguments

```
usage: CodeCrafter.py [-h] [--version] [--encode {base64,rot13,rot47,url,html}]
                      [--decode {base64,hex,url,html}]
                      [--convert {bin-to-hex,bin-to-decimal,hex-to-string}]
                      [--input INPUT] [--file FILE] [--output OUTPUT] [--interactive]

CodeCrafter v1.0.0 - Encoding/Decoding Toolkit

optional arguments:
  -h, --help            show this help message and exit
  --version             show program's version number and exit
  --encode {base64,rot13,rot47,url,html}
                        Encoding operation to perform
  --decode {base64,hex,url,html}
                        Decoding operation to perform
  --convert {bin-to-hex,bin-to-decimal,hex-to-string}
                        Conversion operation to perform
  --input INPUT         Input text to process
  --file FILE           Input file to process
  --output OUTPUT       Output file (default: stdout)
  --interactive         Start interactive mode (default if no other options)
```

## Project Structure

```
encoder_tool/
├── CodeCrafter.py         # Standalone executable script
├── CodeCrafter.bat        # Windows launcher
├── setup.py               # Installation script
├── requirements.txt       # Project dependencies (stdlib only)
├── README.md              # Main documentation
├── INSTALL.md             # Installation guide
├── USAGE_EXAMPLES.md      # Usage examples
├── LICENSE                # MIT license
├── test_codecrafter.py    # Test suite
└── codecrafter/           # Main Python package
    ├── __init__.py        # Package initialization
    ├── __main__.py        # Module entry point (python -m codecrafter)
    ├── main.py            # Main application logic
    ├── banners.py         # ASCII art banners
    └── modules/           # Encoding/decoding modules
        ├── __init__.py
        ├── base64_module.py
        ├── binary_module.py
        ├── hex_module.py
        ├── html_module.py
        ├── rot_module.py
        └── url_module.py
```

## Security Features

### Input Validation
- **Length Limits**: Prevents memory exhaustion attacks (default: 10,000 characters)
- **Type Checking**: Validates input types and formats
- **Sanitization**: Strips whitespace and handles edge cases

### Safe Execution
- **No Shell Injection**: Uses `subprocess` with argument lists
- **No External Commands**: Self-contained Python operations
- **Error Isolation**: Exceptions are caught and handled gracefully

### Example Security Validation
```python
# Input too long
python CodeCrafter.py --encode base64 --input "$(python -c 'print("A"*20000)')"
# Output: Validation Error: Input too long (max 10000 characters)

# Empty input
python CodeCrafter.py --encode base64 --input ""
# Output: Validation Error: Input cannot be empty
```

## Testing

### Manual Testing
```bash
# Test all operations
python CodeCrafter.py --encode base64 --input "Test"
python CodeCrafter.py --decode base64 --input "VGVzdA=="
python CodeCrafter.py --encode url --input "hello world"
python CodeCrafter.py --decode url --input "hello%20world"
```

### Validation Testing
```bash
# Test input validation
python CodeCrafter.py --encode base64 --input ""  # Should fail
echo "Long string..." | python CodeCrafter.py --encode base64 --input "$(cat)"
```

## Contributing

We welcome contributions! Here's how you can help:

### Adding New Encoders
1. Create a new module in the `modules/` directory
2. Implement `encode()` and `decode()` functions
3. Add comprehensive docstrings
4. Update `main.py` to include the new operations
5. Update this README

### Example: Adding a New Encoder
```python
# modules/my_encoder.py
def encode(text):
    """Encode text using my custom algorithm."""
    # Your encoding logic here
    return encoded_text

def decode(encoded_text):
    """Decode text using my custom algorithm."""
    # Your decoding logic here
    return decoded_text
```

### Code Style
- Follow PEP 8 guidelines
- Use type hints where appropriate
- Include comprehensive docstrings
- Handle errors gracefully

## Roadmap

### Version 1.1
- [ ] JSON encoding/decoding
- [ ] Morse code support
- [ ] Caesar cipher with custom shifts
- [ ] ASCII art text generation

### Version 1.2
- [ ] Web interface using Flask
- [ ] REST API endpoints
- [ ] Operation history and favorites
- [ ] Plugin system for custom encoders

### Version 2.0
- [ ] Encryption support (AES, RSA)
- [ ] QR code generation
- [ ] Database storage
- [ ] Multi-language support

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

**@Amanja**

- GitHub: [@Amanja](https://github.com/PtechAmanja)
- Created: 2024

## Acknowledgments

- Inspired by the cybersecurity and CTF community
- Built with Python's excellent standard library
- ASCII art generated using various online tools

## Bug Reports & Feature Requests

Found a bug or have an idea for a new feature? Please:

1. Check existing [issues](https://github.com/PtechAmanja/codecrafter/issues)
2. Create a new issue with detailed information
3. Include steps to reproduce for bugs
4. Provide use cases for feature requests

## Tips & Tricks

### Performance Tips
- For large files, use the `--file` option instead of `--input`
- Chain operations using shell pipes for complex transformations
- Use output files (`--output`) for large results

### Common Use Cases
```bash
# CTF flag submission
python CodeCrafter.py --decode base64 --input "ENCODED_FLAG"

# Web development
python CodeCrafter.py --encode url --input "user@domain.com"

# Data cleaning
python CodeCrafter.py --decode html --file scraped_data.html --output clean_data.txt

# Quick encoding for APIs
curl -d "$(python CodeCrafter.py --encode url --input 'my data')" api.example.com
```

---

**Happy Encoding!** 