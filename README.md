# Markdown to DOCX Web Converter

![CI](https://github.com/blossomz37/ffa-manuscript-to-docx/workflows/CI/CD/badge.svg)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A simple web application that converts Markdown files to DOCX format, specifically designed for ProWriting Aid compatibility.

> **Educational Purpose**: This tool is designed for educational purposes to demonstrate basic scripting and file conversion techniques. It is intended for learning about web development, file processing, and document conversion workflows.
>
> DEMO: https://ffa-manuscript-to-docx.onrender.com/

## Features

- 🌐 **Web Interface**: Upload and convert files through a user-friendly web interface
- 📄 **DOCX Conversion**: Convert to DOCX with proper chapter structure
- 📚 **Multiple Chapter Formats**:
  - `# Chapter N: Title`
  - `## Chapter N. Title` 
  - `# Chapter N` (number only)
- 🔄 **Duplicate Header Handling**: Automatically removes duplicate consecutive chapter headers
- ✅ **ProWriting Aid Compatible**: Uses Heading 2 + Normal styles for perfect compatibility
- 🤖 **MCP Server**: Use with AI assistants like Claude through Model Context Protocol
- 🔒 **Security**: CSRF protection, file validation, and secure temp file handling

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

3. Open your browser and go to `http://localhost:8080`

## Usage

### Web Interface
1. Upload your Markdown file using the web interface
2. Click "Convert to DOCX"
3. Download the converted DOCX file

### MCP Server (AI Assistant Integration)
Use with Claude Desktop or other AI assistants:

```bash
# Install MCP dependencies
pip install -r requirements-mcp.txt

# Test the server
python test_mcp.py
```

Configure in Claude Desktop and ask:
- "Convert this markdown to DOCX format: [your content]"
- "Parse the chapters in this markdown file"
- "Validate this markdown for conversion"

See [MCP_SETUP.md](MCP_SETUP.md) for detailed setup instructions.

## Deployment Options

### Deploy from GitHub to Render (Recommended) 🚀
[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy)

1. Push your code to GitHub
2. Connect your GitHub repo to Render
3. Set environment variable: `SECRET_KEY` (generate with `python -c "import secrets; print(secrets.token_hex(32))"`)
4. Deploy automatically on every push!

### GitHub Pages (Limited Demo)
A basic client-side version is available for GitHub Pages:
1. Enable GitHub Pages in Settings
2. Visit: `https://yourusername.github.io/your-repo/index_static.html`
3. Note: Limited functionality compared to full version

### Local Development
- Run `python app.py` for local testing (runs on port 8080)

See [GITHUB_DEPLOYMENT.md](GITHUB_DEPLOYMENT.md) for detailed deployment instructions

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
