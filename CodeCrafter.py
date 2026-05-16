#!/usr/bin/env python3
"""
CodeCrafter - Standalone executable script

This script can be run directly as:
python CodeCrafter.py
or renamed to CodeCrafter and made executable
"""

import sys
import os

# Add the current directory to path to find the codecrafter package
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, current_dir)

try:
    from codecrafter.main import main
    
    if __name__ == "__main__":
        sys.exit(main())
        
except ImportError as e:
    print(f"Error: Could not import CodeCrafter modules: {e}")
    print("Make sure all files are in the correct location.")
    sys.exit(1)
except Exception as e:
    print(f"Error running CodeCrafter: {e}")
    sys.exit(1) 