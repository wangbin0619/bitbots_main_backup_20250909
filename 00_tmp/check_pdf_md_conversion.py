#!/usr/bin/env python3
"""
Check PDF to Markdown Conversion Completeness

This script compares PDF files in 01_pdf directory with markdown files 
in 02_md directory to verify conversion completeness.

Usage: python check_pdf_md_conversion.py
"""

from pathlib import Path
import os

def check_conversion_completeness():
    """Compare PDF and MD files to check conversion status"""
    
    print("=== PDF to Markdown Conversion Completeness Check ===\n")
    
    # Define directories
    pdf_dir = Path("D:/20-robot/01-bitbots/01_wb_works/01.02_papers/01_pdf")
    md_dir = Path("D:/20-robot/01-bitbots/01_wb_works/01.02_papers/02_md")
    
    # Check if directories exist
    if not pdf_dir.exists():
        print(f"ERROR: PDF directory not found: {pdf_dir}")
        return False
        
    if not md_dir.exists():
        print(f"ERROR: Markdown directory not found: {md_dir}")
        return False
    
    # Get all PDF files
    pdf_files = list(pdf_dir.glob("*.pdf"))
    pdf_stems = {f.stem for f in pdf_files}
    
    # Get all markdown files
    md_files = list(md_dir.glob("*.md")) 
    md_stems = {f.stem for f in md_files}
    
    print(f"PDF Directory: {pdf_dir}")
    print(f"Markdown Directory: {md_dir}")
    print(f"PDF files found: {len(pdf_files)}")
    print(f"Markdown files found: {len(md_files)}")
    print()
    
    # Find converted files (PDF has corresponding MD)
    converted = pdf_stems.intersection(md_stems)
    
    # Find missing conversions (PDF without corresponding MD)
    missing_conversions = pdf_stems - md_stems
    
    # Find extra markdown files (MD without corresponding PDF)
    extra_md_files = md_stems - pdf_stems
    
    # Report results
    print("=== CONVERSION ANALYSIS ===")
    print(f"Successfully converted: {len(converted)}/{len(pdf_files)} ({len(converted)/len(pdf_files)*100:.1f}%)")
    print(f"Missing conversions: {len(missing_conversions)}")
    print(f"Extra markdown files: {len(extra_md_files)}")
    print()
    
    if missing_conversions:
        print("MISSING CONVERSIONS (PDF files without corresponding MD):")
        for i, filename in enumerate(sorted(missing_conversions), 1):
            print(f"  {i:2d}. {filename}")
        print()
    else:
        print("SUCCESS: All PDF files have been converted to markdown!")
        print()
    
    if extra_md_files:
        print("EXTRA MARKDOWN FILES (MD files without corresponding PDF):")
        for i, filename in enumerate(sorted(extra_md_files), 1):
            print(f"  {i:2d}. {filename}")
        print()
    
    # Detailed file size comparison for converted files
    if converted:
        print("=== CONVERSION DETAILS (Sample) ===")
        sample_files = sorted(converted)[:5]  # Show first 5 as sample
        
        for filename in sample_files:
            pdf_file = pdf_dir / f"{filename}.pdf"
            md_file = md_dir / f"{filename}.md"
            
            pdf_size = pdf_file.stat().st_size if pdf_file.exists() else 0
            md_size = md_file.stat().st_size if md_file.exists() else 0
            
            print(f"  {filename[:50]:<50}")
            print(f"    PDF: {pdf_size:>8,} bytes")
            print(f"    MD:  {md_size:>8,} bytes")
            print()
    
    # Summary
    print("=== SUMMARY ===")
    if len(missing_conversions) == 0:
        print("RESULT: COMPLETE - All PDF files successfully converted!")
        return True
    else:
        print(f"RESULT: INCOMPLETE - {len(missing_conversions)} PDF files need conversion")
        return False

if __name__ == "__main__":
    success = check_conversion_completeness()
    exit(0 if success else 1)