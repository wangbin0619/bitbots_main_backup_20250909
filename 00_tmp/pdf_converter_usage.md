# PDF to Markdown Converter Usage Guide

## Overview
Python script that converts PDF files to Markdown format using the `markitdown` library. The output file maintains the same filename with `.md` extension.

## Features
- ✅ Automatic `markitdown` installation if not present
- ✅ Input validation (file exists, is PDF format)
- ✅ Same filename output with `.md` extension
- ✅ Detailed progress reporting
- ✅ Error handling and user-friendly messages
- ✅ File size reporting

## Installation & Requirements
The script automatically installs `markitdown` if needed:
```bash
pip install markitdown
```

## Usage

### Basic Usage
```bash
python pdf_to_markdown_converter.py <input_pdf_file>
```

### Examples
```bash
# Convert a research paper
python pdf_to_markdown_converter.py "research_paper.pdf"
# Output: research_paper.md

# Convert with full path
python pdf_to_markdown_converter.py "D:\20-robot\01-bitbots\01_wb_works\01.02_papers\01_pdf\01 Wolfgang-OP A Robust Humanoid Robot Platform for Research and Competitions.pdf"
# Output: 01 Wolfgang-OP A Robust Humanoid Robot Platform for Research and Competitions.md

# Convert multiple files (using batch script or loop)
for file in *.pdf; do python pdf_to_markdown_converter.py "$file"; done
```

## Output
- Creates `.md` file in the same directory as input PDF
- Preserves original filename (only changes extension)
- UTF-8 encoded markdown text
- Shows file size after conversion

## Error Handling
The script handles:
- Missing input file
- Non-PDF input files
- Installation failures
- Conversion errors
- File permission issues

## Example Output
```
=== PDF to Markdown Converter (using markitdown) ===

🔄 Converting PDF to Markdown...
   Input:  research_paper.pdf
   Output: research_paper.md
✅ Conversion successful!
   Output file: research_paper.md
   File size: 15,234 bytes

🎉 PDF to Markdown conversion completed successfully!
```

## Integration with Bit-Bots Project
Perfect for converting research papers in `01_wb_works/01.02_papers/01_pdf/` to markdown format for easier text processing and analysis.