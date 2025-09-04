# Markdown to DOCX Web Converter

![CI](https://github.com/blossomz37/ffa-manuscript-to-docx/workflows/CI/CD/badge.svg)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A simple web application that converts Markdown files to DOCX format, specifically designed for ProWriting Aid compatibility.

> **Educational Purpose**: This tool is designed for educational purposes to demonstrate basic scripting and file conversion techniques. It is intended for learning about web development, file processing, and document conversion workflows.

## Features

- Upload Markdown files through a web interface
- Convert to DOCX with proper chapter structure
- Supports multiple chapter formats:
  - `# Chapter N: Title`
  - `## Chapter N. Title` 
  - `# Chapter N` (number only)
- Handles duplicate chapter headers automatically
- ProWriting Aid compatible output (Heading 1 + Normal styles)

## Quick Start

1. Clone the repository:
```bash
git clone https://github.com/blossomz37/ffa-manuscript-to-docx.git
cd ffa-manuscript-to-docx
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python app.py
```

4. Open your browser to `http://localhost:8080`

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

## Educational Purpose & Disclaimer

This project is created for **educational purposes only** to demonstrate:
- Basic web development with Flask
- File upload and processing workflows
- Document format conversion techniques
- Simple deployment strategies

**Learning Objectives:**
- Understanding web forms and file handling
- Working with Python libraries (Flask, python-docx)
- Basic HTML templating
- Git version control and GitHub workflows

This tool is intended as a learning resource for students and developers exploring web development and file processing concepts. Use responsibly and in accordance with your educational institution's policies.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
See the deployment section in the documentation for detailed instructions.
