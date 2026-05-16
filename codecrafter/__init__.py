#!/usr/bin/env python3
"""
CodeCrafter - A lightweight Python-based encoding and decoding toolkit

Created by @Amanja
Version: 1.0.0
"""

__version__ = "1.0.0"
__author__ = "Amanja"
__description__ = "A lightweight Python-based encoding and decoding toolkit"

# Import main modules for easy access
from . import modules
from .main import main

__all__ = ['main', 'modules', '__version__', '__author__', '__description__'] 