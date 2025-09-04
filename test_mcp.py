#!/usr/bin/env python3
"""
Test script for the Markdown to DOCX MCP server
"""

import asyncio
import sys
import os

# Add current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

async def test_mcp_server():
    """Test the MCP server functionality"""
    print("🧪 Testing MCP Server for Markdown to DOCX Converter")
    print("=" * 60)
    
    try:
        # Import the server
        from mcp_server import handle_list_tools, handle_call_tool
        print("✅ Successfully imported MCP server")
    except ImportError as e:
        print(f"❌ Failed to import MCP server: {e}")
        print("💡 Install with: pip install mcp")
        return
    
    # Test 1: List available tools
    print("\n📋 Test 1: List Available Tools")
    try:
        tools = await handle_list_tools()
        print(f"✅ Found {len(tools)} tools:")
        for tool in tools:
            print(f"   • {tool.name}: {tool.description}")
    except Exception as e:
        print(f"❌ Error listing tools: {e}")
        return
    
    # Test 2: Validate markdown
    print("\n✅ Test 2: Validate Markdown")
    test_markdown = """# Chapter 1: Introduction
This is the first chapter of our test document.

# Chapter 2: Main Content
Here is the main content with some text.
"""
    
    try:
        result = await handle_call_tool("validate_markdown", {
            "markdown_content": test_markdown
        })
        print(f"✅ Validation result: {result[0].text}")
    except Exception as e:
        print(f"❌ Validation failed: {e}")
    
    # Test 3: Parse chapters
    print("\n📖 Test 3: Parse Chapters")
    try:
        result = await handle_call_tool("parse_markdown_chapters", {
            "markdown_content": test_markdown
        })
        print(f"✅ Chapter parsing result:")
        print(result[0].text)
    except Exception as e:
        print(f"❌ Chapter parsing failed: {e}")
    
    # Test 4: Convert to DOCX
    print("\n🔄 Test 4: Convert to DOCX")
    try:
        result = await handle_call_tool("convert_markdown_to_docx", {
            "markdown_content": test_markdown,
            "output_filename": "test_document"
        })
        print(f"✅ Conversion result:")
        print(result[0].text[:200] + "..." if len(result[0].text) > 200 else result[0].text)
    except Exception as e:
        print(f"❌ Conversion failed: {e}")
    
    print("\n" + "=" * 60)
    print("🎉 MCP Server Test Complete!")
    print("\n💡 To use with Claude Desktop:")
    print("   1. Install dependencies: pip install -r requirements-mcp.txt")
    print("   2. Configure Claude Desktop (see MCP_SETUP.md)")
    print("   3. Restart Claude Desktop")

if __name__ == "__main__":
    asyncio.run(test_mcp_server())