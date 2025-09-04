#!/usr/bin/env python3
"""
Flask web application for Markdown to DOCX conversion
"""

import os
import re
from pathlib import Path
from flask import Flask, request, render_template, send_file, flash, redirect, url_for
from werkzeug.utils import secure_filename
import tempfile
import uuid

try:
    from docx import Document
    from docx.shared import Inches, Pt
    from docx.enum.style import WD_STYLE_TYPE
except ImportError:
    print("Error: python-docx not installed. Install with: pip install python-docx")
    exit(1)

app = Flask(__name__)
app.secret_key = 'your-secret-key-change-this'  # Change this in production
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

UPLOAD_FOLDER = tempfile.gettempdir()
ALLOWED_EXTENSIONS = {'md', 'txt', 'markdown'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def parse_markdown_content(markdown_text):
    """Parse markdown content and extract chapters with their content"""
    chapters = []
    current_chapter = None
    
    lines = markdown_text.split('\n')
    
    for line in lines:
        # Check for chapter heading (supports multiple formats)
        chapter_match = None
        chapter_number = None
        chapter_title = None
        
        # Format 1: # Chapter N: Title or ## Chapter N. Title
        match1 = re.match(r'^##? Chapter (\d+)[:.] (.+)$', line.strip())
        if match1:
            chapter_number = int(match1.group(1))
            chapter_title = match1.group(2).strip()
            chapter_match = True
        else:
            # Format 2: # Chapter N or # CHAPTER N (just number, no title)
            match2 = re.match(r'^# (?:CHAPTER|Chapter) (\d+)$', line.strip())
            if match2:
                chapter_number = int(match2.group(1))
                chapter_title = None  # No title, will be handled in display
                chapter_match = True
        
        if chapter_match:
            # Skip duplicate consecutive chapters (same number)
            if current_chapter and current_chapter['number'] == chapter_number:
                continue
                
            # Save previous chapter if exists
            if current_chapter:
                chapters.append(current_chapter)
            
            # Start new chapter
            current_chapter = {
                'number': chapter_number,
                'title': chapter_title,
                'content_paragraphs': []
            }
        elif line.strip() and current_chapter:
            # Add content paragraph (skip empty lines)
            current_chapter['content_paragraphs'].append(line.strip())
    
    # Add the last chapter
    if current_chapter:
        chapters.append(current_chapter)
    
    return chapters

def create_prowriting_aid_docx(markdown_content, output_path):
    """Create DOCX with exact ProWriting Aid compatible structure"""
    
    # Parse chapters
    chapters = parse_markdown_content(markdown_content)
    
    if not chapters:
        return False, "No chapters found in markdown file"
    
    # Create new document
    doc = Document()
    
    # Clear default styles and ensure we have the right ones
    styles = doc.styles
    
    # Ensure Heading1 style exists and is configured
    try:
        heading1_style = styles['Heading 1']
    except KeyError:
        heading1_style = styles.add_style('Heading 1', WD_STYLE_TYPE.PARAGRAPH)
    
    # Ensure Normal style exists
    try:
        normal_style = styles['Normal']
    except KeyError:
        normal_style = styles.add_style('Normal', WD_STYLE_TYPE.PARAGRAPH)
    
    # Process each chapter
    for i, chapter in enumerate(chapters):
        # Create chapter title, avoiding duplication for number-only chapters
        if chapter['title']:
            chapter_title = f"Chapter {chapter['number']}: {chapter['title']}"
        else:
            chapter_title = f"Chapter {chapter['number']}"
        
        # Add chapter heading with Heading1 style
        heading_para = doc.add_paragraph(chapter_title)
        heading_para.style = 'Heading 1'
        
        # Add CRITICAL empty paragraph with Normal style (matches document.docx)
        empty_para = doc.add_paragraph()
        empty_para.style = 'Normal'
        
        # Add content paragraphs with Normal style
        for content_para in chapter['content_paragraphs']:
            if content_para.strip():  # Skip empty paragraphs
                para = doc.add_paragraph(content_para)
                para.style = 'Normal'
        
        # Add spacing between chapters (except last chapter)
        if i < len(chapters) - 1:
            # Add extra spacing between chapters
            for _ in range(3):
                spacer = doc.add_paragraph()
                spacer.style = 'Normal'
    
    # Save document
    try:
        doc.save(output_path)
        return True, f"Successfully created DOCX with {len(chapters)} chapters"
    except Exception as e:
        return False, f"Error saving DOCX: {str(e)}"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert_file():
    if 'file' not in request.files:
        flash('No file selected')
        return redirect(request.url)
    
    file = request.files['file']
    
    if file.filename == '':
        flash('No file selected')
        return redirect(request.url)
    
    if file and allowed_file(file.filename):
        try:
            # Read markdown content
            markdown_content = file.read().decode('utf-8')
            
            # Create unique filename for output
            unique_id = str(uuid.uuid4())[:8]
            original_name = secure_filename(file.filename)
            base_name = original_name.rsplit('.', 1)[0]
            output_filename = f"{base_name}_converted_{unique_id}.docx"
            output_path = os.path.join(UPLOAD_FOLDER, output_filename)
            
            # Convert to DOCX
            success, message = create_prowriting_aid_docx(markdown_content, output_path)
            
            if success:
                return send_file(output_path, 
                               as_attachment=True, 
                               download_name=output_filename,
                               mimetype='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
            else:
                flash(f'Conversion failed: {message}')
                return redirect(url_for('index'))
                
        except Exception as e:
            flash(f'Error processing file: {str(e)}')
            return redirect(url_for('index'))
    else:
        flash('Invalid file type. Please upload a .md, .txt, or .markdown file.')
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
