#!/usr/bin/env python3
"""
Test script for the Markdown to DOCX converter
Educational testing tool to verify conversion functionality
"""

import os
import sys
import tempfile
from pathlib import Path

# Add the current directory to Python path to import our app
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    from app import create_prowriting_aid_docx
    print("✓ Successfully imported conversion function")
except ImportError as e:
    print(f"✗ Failed to import conversion function: {e}")
    print("Make sure to install dependencies: pip install -r requirements.txt")
    sys.exit(1)

def test_conversion(input_file, output_dir):
    """Test converting a single markdown file"""
    input_path = Path(input_file)
    if not input_path.exists():
        print(f"✗ Test file not found: {input_file}")
        return False
    
    try:
        # Read the markdown content
        with open(input_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Process the content
        output_filename = f"{input_path.stem}_converted.docx"
        output_path = Path(output_dir) / output_filename
        
        # Use a temporary file for processing
        with tempfile.NamedTemporaryFile(mode='w', suffix='.md', delete=False, encoding='utf-8') as temp_file:
            temp_file.write(content)
            temp_file_path = temp_file.name
        
        try:
            # Process the file using the conversion function
            success, message = create_prowriting_aid_docx(content, str(output_path))
            if success:
                print(f"✓ Successfully converted: {input_path.name} → {output_filename}")
                print(f"  Output saved to: {output_path}")
                return True
            else:
                print(f"✗ Conversion failed for: {input_path.name}")
                print(f"  Error: {message}")
                return False
        finally:
            # Clean up temporary file
            os.unlink(temp_file_path)
            
    except Exception as e:
        print(f"✗ Error converting {input_path.name}: {e}")
        return False

def main():
    """Run all conversion tests"""
    print("🧪 Starting Markdown to DOCX Conversion Tests")
    print("=" * 50)
    
    # Set up directories
    test_files_dir = Path("test-files")
    output_dir = Path("test-output")
    
    if not test_files_dir.exists():
        print(f"✗ Test files directory not found: {test_files_dir}")
        return
    
    if not output_dir.exists():
        print(f"Creating output directory: {output_dir}")
        output_dir.mkdir(exist_ok=True)
    
    # Find all markdown test files
    test_files = list(test_files_dir.glob("*.md"))
    
    if not test_files:
        print(f"✗ No test files found in: {test_files_dir}")
        return
    
    print(f"Found {len(test_files)} test files to process")
    print()
    
    # Test each file
    successful_conversions = 0
    total_files = len(test_files)
    
    for test_file in test_files:
        if test_conversion(test_file, output_dir):
            successful_conversions += 1
        print()
    
    # Summary
    print("=" * 50)
    print("🎯 Test Results Summary:")
    print(f"   Total files tested: {total_files}")
    print(f"   Successful conversions: {successful_conversions}")
    print(f"   Failed conversions: {total_files - successful_conversions}")
    
    if successful_conversions == total_files:
        print("🎉 All tests passed!")
    else:
        print("⚠️  Some tests failed. Check the output above for details.")
    
    print(f"\nOutput files saved to: {output_dir.absolute()}")

if __name__ == "__main__":
    main()
