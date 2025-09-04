# Deployment Guide

This guide covers multiple deployment options for the Markdown to DOCX web converter.

## 🚀 Quick Deployment Options

### 1. Render (Recommended - Free Tier)

**Steps:**
1. Fork/upload your code to GitHub
2. Go to [render.com](https://render.com) and sign up
3. Create a new "Web Service"
4. Connect your GitHub repository
5. Configure:
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `python app.py`
   - **Environment:** Python 3
6. Deploy!

**Pros:** Free tier, automatic deployments, SSL included
**Cons:** May sleep when not in use (free tier)

### 2. Railway

**Steps:**
1. Push code to GitHub
2. Go to [railway.app](https://railway.app)
3. Connect GitHub repository
4. Railway auto-detects Python and deploys

**Pros:** Simple setup, good performance
**Cons:** Paid after trial period

### 3. Heroku

**Steps:**
1. Install [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)
2. Create Heroku app:
```bash
heroku create your-app-name
```
3. Deploy:
```bash
git add .
git commit -m "Initial deployment"
git push heroku main
```

**Pros:** Well-established platform
**Cons:** No longer has free tier

### 4. PythonAnywhere

**Steps:**
1. Sign up at [pythonanywhere.com](https://www.pythonanywhere.com)
2. Upload your files via the web interface
3. Create a new web app in the Web tab
4. Configure WSGI file to point to your app

**Pros:** Python-specific, free tier available
**Cons:** Limited features on free tier

### 5. DigitalOcean App Platform

**Steps:**
1. Push code to GitHub
2. Go to DigitalOcean and create an App
3. Connect your repository
4. Configure build and run commands

**Pros:** Scalable, good performance
**Cons:** Paid service

## 🔧 Local Development

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run locally:
```bash
python app.py
```

3. Visit `http://localhost:5000`

## 📝 Configuration Notes

- Change the `secret_key` in `app.py` for production
- The app handles file uploads up to 16MB
- Temporary files are stored in system temp directory
- For production, consider using a proper database for session management

## 🔒 Security Considerations

- Update the Flask secret key
- Consider adding rate limiting for production
- Validate file types and content
- Use HTTPS in production (most platforms provide this automatically)

## 🐳 Docker Deployment (Optional)

Create a `Dockerfile`:
```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python", "app.py"]
```

Build and run:
```bash
docker build -t markdown-converter .
docker run -p 5000:5000 markdown-converter
```
