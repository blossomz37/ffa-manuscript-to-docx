# Deployment Guide for Render.com (Student-Friendly)

## Prerequisites
- GitHub account with your code repository
- Render.com account (free tier available)

## Step-by-Step Deployment

### 1. Prepare Your Repository
Ensure your GitHub repository contains:
- ✅ `app.py` (main application file)
- ✅ `requirements.txt` (Python dependencies)
- ✅ `runtime.txt` (Python version)
- ✅ `templates/` folder with HTML files
- ✅ `render.yaml` (optional, for automatic configuration)

### 2. Create Render Account
1. Go to [render.com](https://render.com)
2. Sign up with your GitHub account
3. Authorize Render to access your repositories

### 3. Deploy Your App
1. Click "New +" → "Web Service"
2. Connect your GitHub repository
3. Configure your service:
   - **Name:** `markdown-to-docx` (or your preference)
   - **Region:** Choose closest to you
   - **Branch:** `main` (or your default branch)
   - **Runtime:** Python 3
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `python app.py`
4. Add environment variable:
   - Click "Advanced" → "Add Environment Variable"
   - **Key:** `SECRET_KEY`
   - **Value:** Click "Generate" or use:
     ```bash
     python -c "import secrets; print(secrets.token_hex(32))"
     ```
5. Click "Create Web Service"

### 4. Wait for Deployment
- Render will build and deploy your app
- This takes 2-5 minutes
- Watch the logs for any errors

### 5. Access Your App
- Once deployed, click the URL at the top of the page
- Format: `https://your-app-name.onrender.com`

## Troubleshooting

### Common Issues

**Build Fails:**
- Check `requirements.txt` has all dependencies
- Ensure Python version in `runtime.txt` is supported

**App Crashes:**
- Check logs in Render dashboard
- Verify `SECRET_KEY` environment variable is set
- Ensure port binding uses `PORT` environment variable

**CSRF Token Errors:**
- Clear browser cookies
- Ensure `SECRET_KEY` is set in environment variables

**File Upload Errors:**
- Check file size (max 16MB)
- Verify file is markdown format (.md, .txt, .markdown)

### Testing Locally First

Before deploying, test locally:
```bash
# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py

# Visit http://localhost:8080
```

## Security Notes for Students

1. **Never commit secrets:** The `SECRET_KEY` should only be in environment variables
2. **Use HTTPS:** Render provides this automatically
3. **Keep dependencies updated:** Regularly update `requirements.txt`
4. **Monitor usage:** Check Render dashboard for resource usage

## Free Tier Limitations

Render's free tier includes:
- ✅ 750 hours/month (enough for continuous running)
- ✅ Automatic HTTPS
- ✅ Automatic deploys from GitHub
- ⚠️ May sleep after 15 minutes of inactivity
- ⚠️ Limited to 512MB RAM

## Next Steps

After successful deployment:
1. Test file conversion with sample markdown files
2. Share your app URL with classmates
3. Monitor logs for any issues
4. Consider adding custom domain (optional)

## Support Resources

- [Render Documentation](https://render.com/docs)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [GitHub Issues](https://github.com/your-username/your-repo/issues)