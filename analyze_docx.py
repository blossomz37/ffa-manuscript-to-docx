#!/usr/bin/env python3
"""
Validation script to examine the generated DOCX files
Educational tool to verify conversion quality
"""

import os
import sys
from pathlib import Path

try:
    from docx import Document
    print("✓ python-docx library available")
except ImportError:
    print("✗ python-docx library not found. Install with: pip install python-docx")
    sys.exit(1)

def analyze_docx_file(filepath):
    """Analyze a DOCX file and report its structure"""
    try:
        doc = Document(filepath)
        
        print(f"\n📄 Analyzing: {filepath.name}")
        print("-" * 40)
        
        paragraphs = doc.paragraphs
        total_paragraphs = len(paragraphs)
        
        # Count different styles
        style_counts = {}
        chapter_count = 0
        
        for para in paragraphs:
            if para.text.strip():  # Only count non-empty paragraphs
                style_name = para.style.name
                style_counts[style_name] = style_counts.get(style_name, 0) + 1
                
                # Count chapters (Heading 1 style)
                if style_name == 'Heading 1':
                    chapter_count += 1
        
        print(f"Total paragraphs: {total_paragraphs}")
        print(f"Chapters found: {chapter_count}")
        print("\nStyle breakdown:")
        
        for style, count in sorted(style_counts.items()):
            print(f"  {style}: {count} paragraphs")
        
        # Show first few paragraphs as examples
        print(f"\nFirst few paragraphs:")
        for i, para in enumerate(paragraphs[:5]):
            if para.text.strip():
                text_preview = para.text[:50] + "..." if len(para.text) > 50 else para.text
                print(f"  {i+1}. [{para.style.name}] {text_preview}")
        
        return True
        
    except Exception as e:
        print(f"✗ Error analyzing {filepath.name}: {e}")
        return False

def main():
    """Analyze all DOCX files in the test output directory"""
    print("🔍 DOCX File Analysis Tool")
    print("=" * 50)
    
    output_dir = Path("test-output")
    
    if not output_dir.exists():
        print(f"✗ Output directory not found: {output_dir}")
        return
    
    docx_files = list(output_dir.glob("*.docx"))
    
    if not docx_files:
        print(f"✗ No DOCX files found in: {output_dir}")
        print("Run the test converter first: python test_converter.py")
        return
    
    print(f"Found {len(docx_files)} DOCX files to analyze")
    
    successful_analyses = 0
    
    for docx_file in sorted(docx_files):
        if analyze_docx_file(docx_file):
            successful_analyses += 1
    
    print("\n" + "=" * 50)
    print(f"📊 Analysis Summary:")
    print(f"   Files analyzed: {len(docx_files)}")
    print(f"   Successful analyses: {successful_analyses}")
    
    if successful_analyses == len(docx_files):
        print("🎉 All files analyzed successfully!")
        print("\n✅ Key things to verify:")
        print("   - Heading 1 style used for chapter titles")
        print("   - Normal style used for paragraph text")
        print("   - Proper chapter count matches source files")
        print("   - Duplicate headers handled correctly")
    else:
        print("⚠️  Some analyses failed. Check the output above.")

if __name__ == "__main__":
    main()
