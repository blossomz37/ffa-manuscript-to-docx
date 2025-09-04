#!/usr/bin/env python3
"""
MCP Server for Markdown to DOCX Converter

This MCP server allows AI assistants to convert Markdown files to DOCX format
through the Model Context Protocol.
"""

import asyncio
import base64
import io
import json
import logging
import os
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app import create_prowriting_aid_docx, validate_markdown_content, parse_markdown_content

# MCP imports
try:
    from mcp.server import Server, NotificationOptions
    from mcp.server.models import InitializationOptions
    import mcp.server.stdio
    import mcp.types as types
except ImportError:
    print("Error: MCP package not installed. Install with: pip install mcp")
    sys.exit(1)

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("markdown-to-docx-mcp")

# Create the MCP server
server = Server("markdown-to-docx")

@server.list_tools()
async def handle_list_tools() -> List[types.Tool]:
    """List available tools for the MCP client."""
    return [
        types.Tool(
            name="convert_markdown_to_docx",
            description="Convert Markdown content to DOCX format with ProWriting Aid compatibility",
            inputSchema={
                "type": "object",
                "properties": {
                    "markdown_content": {
                        "type": "string",
                        "description": "The markdown content to convert"
                    },
                    "output_filename": {
                        "type": "string",
                        "description": "Optional output filename (without extension)",
                        "default": "converted_document"
                    }
                },
                "required": ["markdown_content"]
            }
        ),
        types.Tool(
            name="parse_markdown_chapters",
            description="Parse markdown content and extract chapter structure",
            inputSchema={
                "type": "object",
                "properties": {
                    "markdown_content": {
                        "type": "string",
                        "description": "The markdown content to parse"
                    }
                },
                "required": ["markdown_content"]
            }
        ),
        types.Tool(
            name="validate_markdown",
            description="Validate markdown content for conversion compatibility",
            inputSchema={
                "type": "object",
                "properties": {
                    "markdown_content": {
                        "type": "string",
                        "description": "The markdown content to validate"
                    }
                },
                "required": ["markdown_content"]
            }
        ),
        types.Tool(
            name="convert_file",
            description="Convert a markdown file to DOCX format",
            inputSchema={
                "type": "object",
                "properties": {
                    "file_path": {
                        "type": "string",
                        "description": "Path to the markdown file to convert"
                    },
                    "output_path": {
                        "type": "string",
                        "description": "Optional output path for the DOCX file"
                    }
                },
                "required": ["file_path"]
            }
        )
    ]

@server.call_tool()
async def handle_call_tool(
    name: str, 
    arguments: Optional[Dict[str, Any]] = None
) -> List[types.TextContent | types.ImageContent | types.EmbeddedResource]:
    """Handle tool execution requests."""
    
    if not arguments:
        arguments = {}
    
    try:
        if name == "convert_markdown_to_docx":
            markdown_content = arguments.get("markdown_content", "")
            output_filename = arguments.get("output_filename", "converted_document")
            
            # Validate content
            is_valid, validation_msg = validate_markdown_content(markdown_content)
            if not is_valid:
                return [types.TextContent(
                    type="text",
                    text=f"❌ Validation failed: {validation_msg}"
                )]
            
            # Create temporary output file
            import tempfile
            with tempfile.NamedTemporaryFile(suffix=".docx", delete=False) as tmp:
                output_path = tmp.name
            
            # Convert to DOCX
            success, message = create_prowriting_aid_docx(markdown_content, output_path)
            
            if success:
                # Read the file and encode as base64
                with open(output_path, 'rb') as f:
                    docx_content = f.read()
                
                # Clean up temp file
                os.unlink(output_path)
                
                # Return success with file data
                encoded_content = base64.b64encode(docx_content).decode('utf-8')
                return [types.TextContent(
                    type="text",
                    text=f"✅ {message}\n\nFile: {output_filename}.docx\nSize: {len(docx_content)} bytes\nBase64 content: {encoded_content[:100]}..."
                )]
            else:
                return [types.TextContent(
                    type="text",
                    text=f"❌ Conversion failed: {message}"
                )]
        
        elif name == "parse_markdown_chapters":
            markdown_content = arguments.get("markdown_content", "")
            chapters = parse_markdown_content(markdown_content)
            
            if chapters:
                chapter_list = []
                for ch in chapters:
                    title = f"Chapter {ch['number']}"
                    if ch.get('title'):
                        title += f": {ch['title']}"
                    content_preview = ' '.join(ch['content_paragraphs'][:2])[:100] + "..." if ch['content_paragraphs'] else "No content"
                    chapter_list.append(f"📖 {title}\n   Preview: {content_preview}")
                
                return [types.TextContent(
                    type="text",
                    text=f"Found {len(chapters)} chapters:\n\n" + "\n\n".join(chapter_list)
                )]
            else:
                return [types.TextContent(
                    type="text",
                    text="No chapters found in the markdown content"
                )]
        
        elif name == "validate_markdown":
            markdown_content = arguments.get("markdown_content", "")
            is_valid, validation_msg = validate_markdown_content(markdown_content)
            
            if is_valid:
                chapters = parse_markdown_content(markdown_content)
                return [types.TextContent(
                    type="text",
                    text=f"✅ Valid markdown\n- {len(chapters)} chapters detected\n- Ready for conversion"
                )]
            else:
                return [types.TextContent(
                    type="text",
                    text=f"❌ Invalid: {validation_msg}"
                )]
        
        elif name == "convert_file":
            file_path = arguments.get("file_path", "")
            output_path = arguments.get("output_path", "")
            
            if not os.path.exists(file_path):
                return [types.TextContent(
                    type="text",
                    text=f"❌ File not found: {file_path}"
                )]
            
            # Read file content
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    markdown_content = f.read()
            except Exception as e:
                return [types.TextContent(
                    type="text",
                    text=f"❌ Error reading file: {str(e)}"
                )]
            
            # Validate content
            is_valid, validation_msg = validate_markdown_content(markdown_content)
            if not is_valid:
                return [types.TextContent(
                    type="text",
                    text=f"❌ Validation failed: {validation_msg}"
                )]
            
            # Determine output path
            if not output_path:
                output_path = file_path.rsplit('.', 1)[0] + '_converted.docx'
            
            # Convert to DOCX
            success, message = create_prowriting_aid_docx(markdown_content, output_path)
            
            if success:
                file_size = os.path.getsize(output_path)
                return [types.TextContent(
                    type="text",
                    text=f"✅ {message}\n\nConverted: {file_path}\nOutput: {output_path}\nSize: {file_size} bytes"
                )]
            else:
                return [types.TextContent(
                    type="text",
                    text=f"❌ Conversion failed: {message}"
                )]
        
        else:
            return [types.TextContent(
                type="text",
                text=f"❌ Unknown tool: {name}"
            )]
            
    except Exception as e:
        logger.error(f"Error executing tool {name}: {e}")
        return [types.TextContent(
            type="text",
            text=f"❌ Error: {str(e)}"
        )]

async def main():
    """Main entry point for the MCP server."""
    # Run the server using stdio transport
    async with mcp.server.stdio.stdio_server() as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            InitializationOptions(
                server_name="markdown-to-docx",
                server_version="1.0.0",
                capabilities=server.get_capabilities(
                    notification_options=NotificationOptions(),
                    experimental_capabilities={},
                )
            )
        )

if __name__ == "__main__":
    asyncio.run(main())