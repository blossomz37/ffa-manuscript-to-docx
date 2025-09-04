# Data Directory

This directory is used for persistent data storage when running with Docker Compose.

## Purpose
- Shared storage between web app and MCP server containers
- Persistent data that survives container restarts
- Application-specific data files

## Contents
- User uploaded files (temporary)
- Converted DOCX files
- Application logs (if configured)
- Any other persistent application data

## Volume Mounting
This directory is mounted as `/app/data` in both Docker containers:
- Web App: Uses for temporary file storage and outputs
- MCP Server: Accesses same files for conversion processing

## Development
During development, files created here will persist even when containers are stopped and restarted.
