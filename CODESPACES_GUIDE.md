# GitHub Codespaces Guide

## Should I Use a Separate Branch?

**Short answer: No, use your main branch** ✅

### Why Main Branch is Fine:

1. **Codespaces is just a development environment** - It doesn't change your code
2. **No commits are made automatically** - You control what gets saved
3. **Multiple people can use Codespaces** - Each gets their own isolated environment
4. **Changes are temporary** - Until you commit and push

### When to Use a Separate Branch:

Only create a separate branch if you're:
- 🔧 Experimenting with major changes
- 👥 Working on a new feature
- 🧪 Testing something risky
- 📝 Following your team's git workflow

## Quick Start with Codespaces

### 1. Launch Codespace (Main Branch)
```
1. Go to your GitHub repository
2. Click green "Code" button
3. Select "Codespaces" tab
4. Click "Create codespace on main"
```

### 2. Start the App
In the Codespace terminal:
```bash
# Install dependencies (only needed first time)
pip install -r requirements.txt

# Run the app
python app.py
```

### 3. Access Your App
- Codespaces will show a popup: "Your application running on port 8080 is available"
- Click "Open in Browser"
- Your app is now running!

### 4. Make Changes (Optional)
If you want to experiment:
```bash
# Create a new branch IN Codespaces
git checkout -b experiment-branch

# Make your changes
# Edit files as needed

# If you like the changes, commit them
git add .
git commit -m "Experimental changes from Codespaces"
git push origin experiment-branch
```

### 5. Stop Codespace
- Click "Codespaces" in bottom-left corner
- Select "Stop Current Codespace"
- It auto-saves your work for next time

## Codespaces Best Practices

### ✅ DO:
- Use main branch for normal development
- Let Codespaces auto-save your environment
- Use it for quick testing and demos
- Share the forwarded URL for live demos

### ❌ DON'T:
- Don't commit test files or experiments unless needed
- Don't worry about "messing up" - it's isolated
- Don't keep it running when not using (uses free hours)

## Port Forwarding

Codespaces automatically forwards ports. Your app will be available at:
- **Private URL**: Only you can access (default)
- **Public URL**: Click globe icon to make public (for sharing demos)

To share with others:
1. Click "PORTS" tab in terminal
2. Right-click on port 8080
3. Select "Port Visibility" → "Public"
4. Copy the URL to share

## Configuration File (Optional)

To optimize Codespaces, create `.devcontainer/devcontainer.json`:

```json
{
  "name": "Markdown to DOCX Converter",
  "image": "mcr.microsoft.com/devcontainers/python:3.11",
  "postCreateCommand": "pip install -r requirements.txt",
  "forwardPorts": [8080],
  "customizations": {
    "vscode": {
      "extensions": [
        "ms-python.python",
        "ms-python.vscode-pylance"
      ]
    }
  }
}
```

This will:
- Auto-install dependencies
- Forward port 8080 automatically
- Install helpful VS Code extensions

## Free Tier Limits

GitHub Free includes:
- 120 core hours/month
- 15 GB storage/month
- Sufficient for development and demos

To conserve hours:
- Stop Codespace when done
- Use timeouts (Settings → Codespaces → Default idle timeout)
- Delete old Codespaces you're not using

## Summary

**For your use case:**
1. ✅ Use main branch in Codespaces
2. ✅ Perfect for testing and demos
3. ✅ No risk to your repository
4. ✅ Great for showing your project to others

No separate branch needed unless you're doing experimental development!