# Markdown to DOCX Web Converter

A simple web application that converts Markdown files to DOCX format, specifically designed for ProWriting Aid compatibility.

## Features

- Upload Markdown files through a web interface
- Convert to DOCX with proper chapter structure
- Supports multiple chapter formats:
  - `# Chapter N: Title`
  - `## Chapter N. Title` 
  - `# Chapter N` (number only)
- Handles duplicate chapter headers automatically
- ProWriting Aid compatible output (Heading 1 + Normal styles)

## Installation

1. Install Python dependencies:
```bash
pip install flask python-docx
```

2. Run the application:
```bash
python app.py
```

3. Open your browser and go to `http://localhost:5000`

## Usage

1. Upload your Markdown file using the web interface
2. Click "Convert to DOCX"
3. Download the converted DOCX file

## Deployment Options

### Local Development
- Run `python app.py` for local testing

### Cloud Deployment Options
- **Heroku**: Simple git-based deployment
- **Railway**: Modern platform with automatic deployments
- **Render**: Free tier with easy setup
- **PythonAnywhere**: Python-specific hosting
- **DigitalOcean App Platform**: Scalable cloud hosting

See the deployment section in the documentation for detailed instructions.
