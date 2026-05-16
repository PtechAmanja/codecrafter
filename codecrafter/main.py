#!/usr/bin/env python3

import sys
import subprocess
import argparse
from pathlib import Path
from .banners import get_banner

# Import encoding modules
from .modules import base64_module
from .modules import binary_module
from .modules import hex_module
from .modules import rot_module
from .modules import url_module
from .modules import html_module

# Configuration constants
MAX_INPUT_LENGTH = 10000
# Files are explicitly chosen by the user, so they get a much larger cap
# (the small limit above exists to guard ad-hoc --input arguments).
MAX_FILE_INPUT_LENGTH = 10_000_000
VERSION = "1.0.0"

# Color definitions
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    INFO = '\033[1;34m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# Input validation
def validate_input(text: str, max_length: int = MAX_INPUT_LENGTH) -> str:
    """
    Validate user input without mutating it.

    Args:
        text (str): Input text to validate
        max_length (int): Maximum allowed length
    
    Returns:
        str: Validated input
    
    Raises:
        ValueError: If input is invalid
    """
    if not text:
        raise ValueError("Input cannot be empty")

    if len(text) > max_length:
        raise ValueError(f"Input too long (max {max_length} characters)")

    # Note: input is intentionally returned unmodified. Stripping here would
    # silently corrupt whitespace-significant operations (e.g. ROT47 of " ").
    return text

# Safe screen clearing
def clear_screen():
    """Safely clear the terminal screen using subprocess."""
    try:
        if sys.platform.startswith('win'):
            # 'cls' is a cmd.exe builtin, so it needs the shell; pass it as a
            # string (a list + shell=True is an anti-pattern on Windows).
            subprocess.run('cls', shell=True, check=False)
        else:
            # 'clear' is a real binary, so no shell is required.
            subprocess.run(['clear'], check=False)
    except (OSError, subprocess.SubprocessError):
        # Fallback: print newlines if the clear command is unavailable
        print('\n' * 50)

# Display banner and welcome
def show_intro():
    clear_screen()
    print(f"{bcolors.HEADER}{get_banner()}{bcolors.ENDC}")
    print(f"{bcolors.OKGREEN}Welcome to CodeCrafter v{VERSION}!{bcolors.ENDC}")
    print(f"{bcolors.OKCYAN}Created by @Amanja{bcolors.ENDC}\n")
    print(f"""{bcolors.OKCYAN}
A lightweight Python-based tool that provides a suite of encoding and decoding utilities.
Whether you're handling data transformations, exploring steganography, or solving CTF challenges,
CodeCrafter has your back.
{bcolors.ENDC}""")
    print(f"{bcolors.INFO}Type 'help' for a list of available commands.{bcolors.ENDC}")
    print(f"{bcolors.INFO}Type 'exit' to quit the application.{bcolors.ENDC}")
    print(f"{bcolors.UNDERLINE}-------------------------------------------------------------------------------{bcolors.ENDC}")

# Menu options
def show_menu():
    print(f"{bcolors.INFO}Select an operation:{bcolors.ENDC}")
    print(" 1. Base64 Encode")
    print(" 2. Base64 Decode")
    print(" 3. ROT13")
    print(" 4. ROT47")
    print(" 5. Hex to String")
    print(" 6. Binary to Hex")
    print(" 7. Binary to Decimal")
    print(" 8. URL Encode")
    print(" 9. URL Decode")
    print("10. HTML Entity Encode")
    print("11. HTML Entity Decode")
    print("12. Change Banner")
    print(" 0. Exit")

def safe_input(prompt: str, validate: bool = True) -> str:
    """Get user input with validation."""
    try:
        user_input = input(prompt)
        if validate:
            return validate_input(user_input)
        return user_input
    except ValueError as e:
        print(f"{bcolors.FAIL}Validation Error: {e}{bcolors.ENDC}")
        return ""
    except KeyboardInterrupt:
        print(f"\n{bcolors.WARNING}Operation cancelled by user.{bcolors.ENDC}")
        return ""

class OperationError(Exception):
    """Raised when an operation is unknown or fails."""


# Canonical operation name -> callable producing a str result.
OPERATIONS = {
    "base64_encode": base64_module.encode,
    "base64_decode": base64_module.decode,
    "rot13": rot_module.rot13,
    "rot47": rot_module.rot47,
    "hex_to_string": hex_module.hex_to_string,
    "bin_to_hex": binary_module.bin_to_hex,
    "bin_to_decimal": binary_module.bin_to_decimal,
    "url_encode": url_module.encode,
    "url_decode": url_module.decode,
    "html_encode": html_module.encode,
    "html_decode": html_module.decode,
}


def process_operation(operation: str, text: str) -> str:
    """Run an encoding/decoding operation.

    Returns the result string on success. Raises OperationError if the
    operation name is unknown or the underlying operation raises.
    """
    func = OPERATIONS.get(operation)
    if func is None:
        raise OperationError(f"Unknown operation: {operation}")
    try:
        return func(text)
    except OperationError:
        raise
    except Exception as e:
        raise OperationError(str(e)) from e


def _run_and_print(operation: str, text: str, label: str) -> None:
    """Run an operation for interactive mode, printing success or error."""
    try:
        result = process_operation(operation, text)
        print(f"{bcolors.OKGREEN}{label}: {result}{bcolors.ENDC}")
    except OperationError as e:
        print(f"{bcolors.FAIL}Error: {e}{bcolors.ENDC}")

def parse_arguments():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description=f'CodeCrafter v{VERSION} - Encoding/Decoding Toolkit',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python CodeCrafter.py --encode base64 --input "Hello World"
  python CodeCrafter.py --decode base64 --input "SGVsbG8gV29ybGQ="
  python CodeCrafter.py --encode url --input "hello world"
  python CodeCrafter.py --file input.txt --encode base64
        """
    )
    
    parser.add_argument('--version', action='version', version=f'CodeCrafter v{VERSION}')
    
    # Operation type
    operation_group = parser.add_mutually_exclusive_group()
    operation_group.add_argument('--encode', 
                                choices=['base64', 'rot13', 'rot47', 'url', 'html'],
                                help='Encoding operation to perform')
    operation_group.add_argument('--decode', 
                                choices=['base64', 'hex', 'url', 'html'],
                                help='Decoding operation to perform')
    operation_group.add_argument('--convert',
                                choices=['bin-to-hex', 'bin-to-decimal', 'hex-to-string'],
                                help='Conversion operation to perform')
    
    # Input source
    input_group = parser.add_mutually_exclusive_group()
    input_group.add_argument('--input', type=str, help='Input text to process')
    input_group.add_argument('--file', type=Path, help='Input file to process')
    
    # Output options
    parser.add_argument('--output', type=Path, help='Output file (default: stdout)')
    parser.add_argument('--interactive', action='store_true', 
                       help='Start interactive mode (default if no other options)')
    
    return parser.parse_args()

def cli_mode(args):
    """Handle command-line interface mode."""
    # Determine operation
    encode_ops = {
        "base64": "base64_encode",
        "rot13": "rot13",
        "rot47": "rot47",
        "url": "url_encode",
        "html": "html_encode",
    }
    decode_ops = {
        "base64": "base64_decode",
        "hex": "hex_to_string",
        "url": "url_decode",
        "html": "html_decode",
    }
    if args.encode:
        operation = encode_ops[args.encode]
        operation_name = f"{args.encode.upper()} Encode"
    elif args.decode:
        operation = decode_ops[args.decode]
        operation_name = f"{args.decode.upper()} Decode"
    elif args.convert:
        operation = args.convert.replace('-', '_')
        operation_name = args.convert.replace('-', ' ').title()
    else:
        print(f"{bcolors.FAIL}Error: No operation specified{bcolors.ENDC}")
        return 1
    
    # Get input text
    if args.file:
        try:
            with open(args.file, 'r', encoding='utf-8') as f:
                input_text = f.read()
        except FileNotFoundError:
            print(f"{bcolors.FAIL}Error: File '{args.file}' not found{bcolors.ENDC}")
            return 1
        except Exception as e:
            print(f"{bcolors.FAIL}Error reading file: {e}{bcolors.ENDC}")
            return 1
        max_len = MAX_FILE_INPUT_LENGTH
    elif args.input:
        input_text = args.input
        max_len = MAX_INPUT_LENGTH
    else:
        print(f"{bcolors.FAIL}Error: No input specified (use --input or --file){bcolors.ENDC}")
        return 1

    # Validate input
    try:
        validated_input = validate_input(input_text, max_len)
    except ValueError as e:
        print(f"{bcolors.FAIL}Validation Error: {e}{bcolors.ENDC}")
        return 1
    
    # Process operation
    try:
        result = process_operation(operation, validated_input)
    except OperationError as e:
        print(f"{bcolors.FAIL}Error: {e}{bcolors.ENDC}")
        return 1

    # Output result
    if args.output:
        try:
            with open(args.output, 'w', encoding='utf-8') as f:
                f.write(result)
            print(f"{bcolors.OKGREEN}Result written to '{args.output}'{bcolors.ENDC}")
        except Exception as e:
            print(f"{bcolors.FAIL}Error writing to file: {e}{bcolors.ENDC}")
            return 1
    else:
        print(f"{bcolors.OKGREEN}{operation_name}: {result}{bcolors.ENDC}")
    
    return 0

# Main interactive loop
def interactive_mode():
    """Run the interactive CLI interface."""
    show_intro()
    
    while True:
        show_menu()
        choice = input(f"{bcolors.BOLD}Choice > {bcolors.ENDC}")

        if choice == "1":
            text = safe_input("Enter text to encode (Base64): ")
            if text:
                _run_and_print("base64_encode", text, "Encoded")
                
        elif choice == "2":
            text = safe_input("Enter Base64 to decode: ")
            if text:
                _run_and_print("base64_decode", text, "Decoded")
                
        elif choice == "3":
            text = safe_input("Enter text for ROT13: ")
            if text:
                _run_and_print("rot13", text, "ROT13")
                
        elif choice == "4":
            text = safe_input("Enter text for ROT47: ")
            if text:
                _run_and_print("rot47", text, "ROT47")
                
        elif choice == "5":
            hex_input = safe_input("Enter hex string to convert: ")
            if hex_input:
                _run_and_print("hex_to_string", hex_input, "String")
                
        elif choice == "6":
            bin_input = safe_input("Enter binary to convert to hex: ")
            if bin_input:
                _run_and_print("bin_to_hex", bin_input, "Hex")
                
        elif choice == "7":
            bin_input = safe_input("Enter binary to convert to decimal: ")
            if bin_input:
                _run_and_print("bin_to_decimal", bin_input, "Decimal")
                
        elif choice == "8":
            text = safe_input("Enter text to URL encode: ")
            if text:
                _run_and_print("url_encode", text, "URL Encoded")
                
        elif choice == "9":
            text = safe_input("Enter URL to decode: ")
            if text:
                _run_and_print("url_decode", text, "URL Decoded")
                
        elif choice == "10":
            text = safe_input("Enter text to HTML encode: ")
            if text:
                _run_and_print("html_encode", text, "HTML Encoded")
                
        elif choice == "11":
            text = safe_input("Enter HTML entities to decode: ")
            if text:
                _run_and_print("html_decode", text, "HTML Decoded")
                
        elif choice == "12":
            clear_screen()
            show_intro()
            continue
            
        elif choice.strip().lower() in ("0", "exit"):
            print(f"{bcolors.WARNING}Exiting CodeCrafter...{bcolors.ENDC}")
            sys.exit(0)
        else:
            print(f"{bcolors.FAIL}Invalid option. Please try again.{bcolors.ENDC}")

        input(f"\n{bcolors.OKBLUE}Press Enter to continue...{bcolors.ENDC}")
        clear_screen()
        show_intro()

# Entry point
def main():
    """Main entry point."""
    args = parse_arguments()
    
    # If CLI arguments are provided, use CLI mode
    if args.encode or args.decode or args.convert:
        return cli_mode(args)
    else:
        # Default to interactive mode
        interactive_mode()
        return 0

if __name__ == "__main__":
    sys.exit(main())
