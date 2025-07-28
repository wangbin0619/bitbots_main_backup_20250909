# Utilities Directory

This directory contains utility scripts and tools for the Bit-Bots project workflow.

## Available Tools

### PDF to Markdown Converter
**File:** `pdf_to_markdown_converter.py`  
**Purpose:** Convert PDF files to Markdown format with same filename  
**Usage:** `python pdf_to_markdown_converter.py <input_pdf_file>`  
**Documentation:** See `pdf_converter_usage.md` for detailed instructions

**Features:**
- Auto-installs markitdown dependency
- Input validation and error handling  
- UTF-8 safe markdown output
- Progress reporting
- Same filename with .md extension

**Example:**
```bash
cd D:\20-robot\01-bitbots\01_wb_works\01.03_utilities
python pdf_to_markdown_converter.py "../01.02_papers/01_pdf/research_paper.pdf"
# Output: ../01.02_papers/01_pdf/research_paper.md
```

## Adding New Utilities

When adding new utility scripts:
1. Place script files in this directory
2. Include documentation (README or usage file)
3. Update this README.md file
4. Consider updating CLAUDE.local.md if the tool should be reused instead of regenerated