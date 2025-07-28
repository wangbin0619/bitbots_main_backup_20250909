#!/usr/bin/env python3
"""
PDF to Markdown Converter using markitdown

This script converts PDF files to Markdown format using the markitdown library.
The output file will have the same name as input but with .md extension.

Usage:
    python pdf_to_markdown_converter.py <input_pdf_file>

Example:
    python pdf_to_markdown_converter.py "research_paper.pdf"
    # Outputs: research_paper.md

Requirements:
    pip install markitdown

Author: Generated for Bit-Bots project
"""

import sys
import os
from pathlib import Path

def install_markitdown():
    """Install markitdown if not available"""
    try:
        import markitdown
        return True
    except ImportError:
        print("markitdown not found. Installing...")
        import subprocess
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "markitdown"])
            print("markitdown installed successfully!")
            return True
        except subprocess.CalledProcessError as e:
            print(f"Failed to install markitdown: {e}")
            return False

def convert_pdf_to_markdown(pdf_path):
    """
    Convert PDF file to Markdown using markitdown
    
    Args:
        pdf_path (str): Path to the input PDF file
        
    Returns:
        bool: True if conversion successful, False otherwise
    """
    try:
        from markitdown import MarkItDown
    except ImportError:
        print("markitdown library not available after installation attempt")
        return False
    
    # Validate input file
    pdf_file = Path(pdf_path)
    if not pdf_file.exists():
        print(f"Error: PDF file not found: {pdf_path}")
        return False
    
    if not pdf_file.suffix.lower() == '.pdf':
        print(f"Error: Input file is not a PDF: {pdf_path}")
        return False
    
    # Create output path with same name but .md extension
    output_path = pdf_file.with_suffix('.md')
    
    print(f"Converting PDF to Markdown...")
    print(f"   Input:  {pdf_file}")
    print(f"   Output: {output_path}")
    
    try:
        # Initialize MarkItDown converter
        md = MarkItDown()
        
        # Convert PDF to markdown
        result = md.convert(str(pdf_file))
        
        # Write markdown content to output file
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(result.text_content)
        
        print(f"Conversion successful!")
        print(f"   Output file: {output_path}")
        print(f"   File size: {output_path.stat().st_size:,} bytes")
        
        return True
        
    except Exception as e:
        print(f"Error during conversion: {e}")
        return False

def main():
    """Main function to handle command line arguments and execute conversion"""
    print("=== PDF to Markdown Converter (using markitdown) ===\n")
    
    # Check command line arguments
    if len(sys.argv) != 2:
        print("Usage: python pdf_to_markdown_converter.py <input_pdf_file>")
        print("\nExample:")
        print('   python pdf_to_markdown_converter.py "research_paper.pdf"')
        sys.exit(1)
    
    pdf_path = sys.argv[1]
    
    # Install markitdown if needed
    if not install_markitdown():
        print("Cannot proceed without markitdown library")
        sys.exit(1)
    
    # Convert PDF to Markdown
    success = convert_pdf_to_markdown(pdf_path)
    
    if success:
        print("\nPDF to Markdown conversion completed successfully!")
        sys.exit(0)
    else:
        print("\nPDF to Markdown conversion failed!")
        sys.exit(1)

if __name__ == "__main__":
    main()