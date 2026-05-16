#!/usr/bin/env python3

from setuptools import setup, find_packages
import os

# Read README for long description
def read_readme():
    with open("README.md", "r", encoding="utf-8") as fh:
        return fh.read()

# Read requirements
def read_requirements():
    """Read requirements from requirements.txt, excluding comments and dev dependencies."""
    try:
        with open("requirements.txt", "r", encoding="utf-8") as fh:
            lines = fh.readlines()
        
        # Filter out comments, empty lines, and dev dependencies
        requirements = []
        for line in lines:
            line = line.strip()
            if line and not line.startswith('#') and not line.startswith('pytest') and not line.startswith('black') and not line.startswith('flake8') and not line.startswith('mypy'):
                requirements.append(line)
        
        return requirements
    except FileNotFoundError:
        return []

setup(
    name="codecrafter",
    version="1.0.0",
    author="Amanja",
    author_email="pappyiepinkie@gmail.com",
    description="A lightweight Python-based encoding and decoding toolkit",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://github.com/PtechAmanja/codecrafter",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Topic :: Security",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Text Processing",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
        "Environment :: Console",
    ],
    python_requires=">=3.6",
    install_requires=read_requirements(),
    extras_require={
        "dev": [
            "pytest>=6.0.0",
            "black>=21.0.0",
            "flake8>=3.8.0",
            "mypy>=0.910",
        ],
    },
    entry_points={
        "console_scripts": [
            "codecrafter=codecrafter.main:main",
            "CodeCrafter=codecrafter.main:main",
        ],
    },
    include_package_data=True,
    package_data={
        "codecrafter": ["*.py"],
    },
    keywords="encoding decoding base64 url html rot13 rot47 binary hex ctf security",
    project_urls={
        "Bug Reports": "https://github.com/PtechAmanja/codecrafter/issues",
        "Source": "https://github.com/PtechAmanja/codecrafter",
        "Documentation": "https://github.com/PtechAmanja/codecrafter/blob/main/README.md",
    },
) 