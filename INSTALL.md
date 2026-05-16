# CodeCrafter Installation Guide

This guide explains the different ways to install and run CodeCrafter.

## Quick Start (No Installation Required)

### Method 1: Direct Execution (Recommended)
```bash
# Download/clone the repository
git clone https://github.com/PtechAmanja/codecrafter.git
cd codecrafter

# Run directly
python CodeCrafter.py --version
```

### Method 2: Windows Batch File
```cmd
# Windows users can use the batch file
CodeCrafter.bat --version
```

### Method 3: Python Module
```bash
# Run as a Python module
python -m codecrafter --version
```

## Installation Methods

### Method A: Pip Install (Development Mode)
```bash
# Clone the repository
git clone https://github.com/PtechAmanja/codecrafter.git
cd codecrafter

# Install in development mode
pip install -e .

# Now you can run from anywhere
codecrafter --version
# or
CodeCrafter --version
```

### Method B: Manual Installation
```bash
# Clone the repository
git clone https://github.com/PtechAmanja/codecrafter.git
cd codecrafter

# Copy to your preferred location
cp -r codecrafter /usr/local/lib/python3.x/site-packages/
cp CodeCrafter.py /usr/local/bin/codecrafter
chmod +x /usr/local/bin/codecrafter
```

### Method C: Add to PATH (Windows)
```cmd
# Add the CodeCrafter directory to your Windows PATH
# Then you can run from anywhere:
CodeCrafter.bat --version
```

### Method D: Add to PATH (Linux/macOS)
```bash
# Add to your .bashrc, .zshrc, or .profile
export PATH="$PATH:/path/to/codecrafter"

# Make the script executable
chmod +x CodeCrafter.py

# Create an alias (optional)
alias codecrafter='python /path/to/codecrafter/CodeCrafter.py'
```

## Usage Examples

### Command Line Usage
```bash
# Using the standalone script
python CodeCrafter.py --encode base64 --input "Hello World"

# Using the batch file (Windows)
CodeCrafter.bat --encode url --input "hello world"

# Using the installed version
codecrafter --encode html --input "<script>test</script>"
```

### Interactive Mode
```bash
# All methods support interactive mode
python CodeCrafter.py
# or
CodeCrafter.bat
# or
codecrafter
```

## Linux/macOS Specific Setup

### Create a System-Wide Command
```bash
# Copy the script to a system directory
sudo cp CodeCrafter.py /usr/local/bin/codecrafter
sudo chmod +x /usr/local/bin/codecrafter

# Now run from anywhere
codecrafter --version
```

### Create a User Command
```bash
# Copy to user's local bin
mkdir -p ~/.local/bin
cp CodeCrafter.py ~/.local/bin/codecrafter
chmod +x ~/.local/bin/codecrafter

# Add to PATH if not already
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc

# Now run from anywhere
codecrafter --version
```

## Windows Specific Setup

### PowerShell Execution Policy
If you get execution policy errors:
```powershell
# Allow local scripts
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Then run
.\CodeCrafter.bat --version
```

### Add to Windows PATH
1. Right-click "This PC" → Properties
2. Advanced System Settings → Environment Variables
3. Add the CodeCrafter directory to PATH
4. Restart Command Prompt/PowerShell
5. Run `CodeCrafter.bat --version` from anywhere

### Create Windows Shortcut
```cmd
# Create a shortcut that runs
python "C:\path\to\codecrafter\CodeCrafter.py"
```

## Verification

Test your installation with these commands:
```bash
# Check version
codecrafter --version
# or
python CodeCrafter.py --version

# Test encoding
codecrafter --encode base64 --input "test"
# Expected: BASE64 Encode: dGVzdA==

# Test interactive mode
codecrafter
# Should show the colorful menu
```

## Troubleshooting

### Common Issues

#### "Command not found"
- Make sure Python is in your PATH
- Verify the file permissions (executable)
- Check if the script location is in your PATH

#### "Module not found" errors
- Ensure all files are in the correct directory structure
- Check that the `codecrafter` package directory exists
- Verify Python version (requires 3.6+)

#### Permission denied (Linux/macOS)
```bash
chmod +x CodeCrafter.py
# or
chmod +x /path/to/codecrafter
```

#### Windows PowerShell execution policy
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Getting Help
```bash
# Show all available options
codecrafter --help
# or
python CodeCrafter.py --help
```

## Directory Structure After Installation

```
codecrafter/
├── CodeCrafter.py          # Standalone executable script
├── CodeCrafter.bat        # Windows batch file
├── setup.py               # Installation script
├── requirements.txt       # Dependencies
├── README.md             # Main documentation
├── INSTALL.md            # This file
└── codecrafter/          # Python package
    ├── __init__.py       # Package init
    ├── __main__.py       # Module entry point
    ├── main.py          # Main application logic
    ├── banners.py       # ASCII banners
    └── modules/         # Encoding modules
        ├── __init__.py
        ├── base64_module.py
        ├── binary_module.py
        ├── hex_module.py
        ├── html_module.py
        ├── rot_module.py
        └── url_module.py
```

## Success!

If you can run `codecrafter --version` and see `CodeCrafter v1.0.0`, you're all set!

Now you can use CodeCrafter from anywhere on your system. 