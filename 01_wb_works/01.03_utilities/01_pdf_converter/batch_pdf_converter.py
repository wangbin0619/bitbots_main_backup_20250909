#!/usr/bin/env python3
"""
Batch PDF to Markdown Converter for Bit-Bots Papers

This script converts all PDF files in the papers directory to markdown format
using the existing PDF converter utility.

Usage: python batch_pdf_converter.py
"""

import os
import subprocess
import sys
from pathlib import Path

def main():
    """Convert all PDFs in the papers directory to markdown"""
    
    print("=== Batch PDF to Markdown Converter ===\n")
    
    # Define paths
    pdf_dir = Path("D:/20-robot/01-bitbots/01_wb_works/01.02_papers/01_pdf")
    converter_script = Path("D:/20-robot/01-bitbots/01_wb_works/01.03_utilities/01_pdf_converter/pdf_to_markdown_converter.py")
    
    # Validate paths
    if not pdf_dir.exists():
        print(f"Error: PDF directory not found: {pdf_dir}")
        sys.exit(1)
        
    if not converter_script.exists():
        print(f"Error: Converter script not found: {converter_script}")
        sys.exit(1)
    
    # Find all PDF files
    pdf_files = list(pdf_dir.glob("*.pdf"))
    if not pdf_files:
        print(f"No PDF files found in {pdf_dir}")
        sys.exit(0)
    
    print(f"Found {len(pdf_files)} PDF files to convert:\n")
    
    # Convert each PDF file
    successful = 0
    failed = 0
    
    for i, pdf_file in enumerate(pdf_files, 1):
        print(f"[{i}/{len(pdf_files)}] Converting: {pdf_file.name}")
        
        try:
            # Run the converter script
            result = subprocess.run([
                sys.executable, 
                str(converter_script), 
                str(pdf_file)
            ], capture_output=True, text=True, timeout=300)  # 5 minute timeout per file
            
            if result.returncode == 0:
                print(f"  SUCCESS: {pdf_file.stem}.md")
                successful += 1
            else:
                print(f"  FAILED: {result.stderr.strip()}")
                failed += 1
                
        except subprocess.TimeoutExpired:
            print(f"  TIMEOUT: Conversion took too long")
            failed += 1
        except Exception as e:
            print(f"  ERROR: {e}")
            failed += 1
        
        print()  # Add blank line between files
    
    # Summary
    print("=== Conversion Summary ===")
    print(f"Total files: {len(pdf_files)}")
    print(f"Successful: {successful}")
    print(f"Failed: {failed}")
    
    if successful > 0:
        print(f"\nMarkdown files created in: {pdf_dir}")
    
    sys.exit(0 if failed == 0 else 1)

if __name__ == "__main__":
    main()