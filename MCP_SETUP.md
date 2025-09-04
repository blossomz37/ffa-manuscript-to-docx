# MCP Server Setup Guide

## What is MCP?

The Model Context Protocol (MCP) allows AI assistants like Claude to interact with external tools and services. This MCP server makes your Markdown to DOCX converter available to AI assistants for direct document conversion.

## Features

The MCP server provides these tools to AI assistants:

🔧 **convert_markdown_to_docx** - Convert markdown content to DOCX format
📖 **parse_markdown_chapters** - Extract and analyze chapter structure  
✅ **validate_markdown** - Check if markdown is ready for conversion
📄 **convert_file** - Convert a markdown file from disk

## Installation

### 1. Install MCP Dependencies

```bash
# Install MCP package and dependencies
pip install -r requirements-mcp.txt

# Or install manually
pip install mcp python-docx Flask Flask-WTF
```

### 2. Test the Server

```bash
# Test the MCP server directly
python mcp_server.py
```

If working correctly, it will wait for MCP protocol messages.

## Configuration for Claude Desktop

### 1. Find Your Configuration Directory

**macOS:**
```
~/Library/Application Support/Claude/claude_desktop_config.json
```

**Windows:**
```
%APPDATA%\Claude\claude_desktop_config.json
```

**Linux:**
```
~/.config/Claude/claude_desktop_config.json
```

### 2. Add MCP Server Configuration

Edit `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "markdown-to-docx": {
      "command": "python",
      "args": ["/path/to/your/project/mcp_server.py"],
      "env": {
        "PYTHONPATH": "/path/to/your/project"
      }
    }
  }
}
```

**Replace `/path/to/your/project/` with your actual project path.**

### 3. Restart Claude Desktop

Close and restart Claude Desktop to load the new configuration.

## Usage Examples

Once configured, you can ask Claude to convert documents:

### Basic Conversion
```
"Convert this markdown to DOCX format:

# Chapter 1: Introduction
This is my first chapter.

# Chapter 2: Main Content  
Here's the main content."
```

### File Conversion
```
"Please convert the markdown file at /path/to/my/story.md to DOCX format"
```

### Chapter Analysis
```
"Parse the chapters in this markdown and tell me about the structure:
[your markdown content]"
```

### Validation
```
"Check if this markdown is ready for DOCX conversion:
[your markdown content]"
```

## Troubleshooting

### Server Not Found
```
❌ Error: MCP server not responding
```

**Solutions:**
1. Check the file path in `claude_desktop_config.json`
2. Ensure Python and dependencies are installed
3. Test the server manually: `python mcp_server.py`

### Import Errors
```
❌ Error: No module named 'mcp'
```

**Solution:**
```bash
pip install mcp
```

### Path Issues
```
❌ Error: No module named 'app'
```

**Solution:**
Ensure the `PYTHONPATH` in config points to your project directory.

### Permission Issues
```
❌ Error: Permission denied
```

**Solutions:**
1. Check file permissions
2. Use absolute paths in configuration
3. Run Claude Desktop as administrator (Windows)

## Development Mode

For development and testing:

### Manual Testing
```bash
# Test conversion function
python -c "
import sys
sys.path.append('.')
from mcp_server import *
import asyncio

async def test():
    tools = await handle_list_tools()
    print(f'Available tools: {len(tools)}')
    for tool in tools:
        print(f'- {tool.name}: {tool.description}')

asyncio.run(test())
"
```

### Debug Mode
Add logging to see what's happening:

```python
# Add to mcp_server.py
import logging
logging.basicConfig(level=logging.DEBUG)
```

## Advanced Configuration

### Custom Python Environment
If using a virtual environment:

```json
{
  "mcpServers": {
    "markdown-to-docx": {
      "command": "/path/to/venv/bin/python",
      "args": ["/path/to/project/mcp_server.py"],
      "env": {
        "PYTHONPATH": "/path/to/project"
      }
    }
  }
}
```

### Multiple Servers
You can run multiple MCP servers:

```json
{
  "mcpServers": {
    "markdown-to-docx": {
      "command": "python",
      "args": ["/path/to/markdown-converter/mcp_server.py"]
    },
    "other-tool": {
      "command": "python",
      "args": ["/path/to/other-tool/server.py"]
    }
  }
}
```

## Security Notes

- The MCP server runs locally with your user permissions
- It can read/write files in your system
- Only give Claude access to directories you trust
- Consider using a sandboxed environment for production use

## Contributing

To improve the MCP server:

1. Fork the repository
2. Modify `mcp_server.py`
3. Test with Claude Desktop
4. Submit a pull request

## Support

- Check the [MCP documentation](https://github.com/modelcontextprotocol/python-sdk)
- Open issues on GitHub
- Test with `python mcp_server.py` for debugging