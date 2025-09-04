# Test Files

This directory contains sample Markdown files for testing the conversion functionality.

## Test Files Description

### `sample-story.md`
- **Format**: `# Chapter N: Title`
- **Content**: Multi-paragraph story with descriptive chapter titles
- **Tests**: Standard chapter format with colons

### `academy-story.md`
- **Format**: `## Chapter N. Title`
- **Content**: School-based story with period separators
- **Tests**: Alternative chapter format with periods and H2 headers

### `simple-chapters.md`
- **Format**: `# Chapter N`
- **Content**: Simple numbered chapters without titles
- **Tests**: Minimal chapter format (numbers only)

### `duplicate-headers.md`
- **Format**: Mixed with duplicate chapter headers
- **Content**: Story with intentionally duplicated chapter names
- **Tests**: Duplicate header handling functionality

## Running Tests

To test the conversion functionality:

```bash
# Install dependencies first
pip install -r requirements.txt

# Run the test script
python test_converter.py
```

The test script will:
1. Process all `.md` files in this directory
2. Convert them to DOCX format
3. Save outputs to the `test-output/` directory
4. Report success/failure for each conversion

## Expected Behavior

The converter should:
- ✅ Handle all three chapter formats correctly
- ✅ Convert duplicate headers by appending numbers
- ✅ Maintain paragraph structure and formatting
- ✅ Create ProWritingAid-compatible DOCX files
- ✅ Use appropriate heading styles (Heading 1 for chapters)

## Educational Purpose

These test files demonstrate various scenarios you might encounter when processing manuscript files, helping you understand how the conversion logic handles different formats and edge cases.
