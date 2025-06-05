# 🚀 PVTG Dashboard Deployment Guide

## Option 1: Streamlit Cloud (Recommended - Free & Easy)

### Prerequisites:
- GitHub account
- Your dashboard files

### Steps:

1. **Create GitHub Repository**
   ```bash
   # Initialize git in your dashboard folder
   git init
   git add .
   git commit -m "Initial commit: PVTG Survey Dashboard"
   
   # Create repository on GitHub and push
   git remote add origin https://github.com/YOUR_USERNAME/pvtg-dashboard.git
   git push -u origin main
   ```

2. **Deploy on Streamlit Cloud**
   - Visit [share.streamlit.io](https://share.streamlit.io)
   - Sign in with GitHub
   - Click "New app"
   - Select your repository: `YOUR_USERNAME/pvtg-dashboard`
   - Set main file path: `dashboard.py`
   - Click "Deploy"

3. **Your app will be live at**: `https://YOUR_USERNAME-pvtg-dashboard-dashboard-xyz123.streamlit.app`

### ✅ Pros:
- Completely free
- Easy setup
- Automatic updates when you push to GitHub
- SSL certificate included

### ❌ Cons:
- Public by default (though you have authentication)
- Limited resources (1GB RAM)

---

## Option 2: Railway (Modern & Simple)

### Steps:

1. **Install Railway CLI**
   ```bash
   npm install -g @railway/cli
   # or
   curl -fsSL https://railway.app/install.sh | sh
   ```

2. **Login and Deploy**
   ```bash
   railway login
   railway init
   railway add
   railway deploy
   ```

3. **Configure Environment**
   - Railway will auto-detect your Python app
   - Custom domain available
   - Environment variables can be set in dashboard

### Cost: $5/month for hobby plan

---

## Option 3: Heroku

### Prerequisites:
- Heroku account
- Heroku CLI installed

### Additional Files Needed:

Create these files in your dashboard directory:

**Procfile:**
```
web: streamlit run dashboard.py --server.port=$PORT --server.address=0.0.0.0
```

**runtime.txt:**
```
python-3.11.2
```

### Deploy Steps:
```bash
# Login to Heroku
heroku login

# Create Heroku app
heroku create pvtg-survey-dashboard

# Deploy
git add .
git commit -m "Deploy to Heroku"
git push heroku main

# Open your app
heroku open
```

### Cost: $7/month for basic dyno

---

## Option 4: DigitalOcean App Platform

### Steps:

1. **Create DigitalOcean Account**
2. **Use App Platform**
   - Connect your GitHub repository
   - Select "Web Service"
   - Configure:
     - Build Command: `pip install -r requirements.txt`
     - Run Command: `streamlit run dashboard.py --server.port=$PORT --server.address=0.0.0.0`

### Cost: $5/month for basic plan

---

## Option 5: Local Network Deployment

For internal use within your organization:

### Run on Local Server:
```bash
# Run on all network interfaces
streamlit run dashboard.py --server.address=0.0.0.0 --server.port=8501

# Access from other computers on same network
http://YOUR_LOCAL_IP:8501
```

### Find Your Local IP:
```bash
# On Mac/Linux
ifconfig | grep "inet " | grep -v 127.0.0.1

# On Windows
ipconfig | findstr "IPv4"
```

---

## Option 6: Docker Deployment

### Create Dockerfile:
```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "dashboard.py", "--server.address=0.0.0.0", "--server.port=8501"]
```

### Build and Run:
```bash
# Build Docker image
docker build -t pvtg-dashboard .

# Run container
docker run -p 8501:8501 pvtg-dashboard
```

---

## Pre-Deployment Checklist

### 1. **Prepare Your Files**
- ✅ dashboard.py
- ✅ requirements.txt
- ✅ 7 Villages PVTGs survey - 2025.xlsx
- ✅ README.md

### 2. **Security Considerations**
- ✅ Authentication is already implemented
- ✅ Consider changing default passwords
- ✅ Add environment variables for sensitive data

### 3. **Performance Optimization**
- ✅ Data caching is already implemented
- ✅ Consider compressing Excel file if too large
- ✅ Optimize images/visualizations

---

## Environment Variables (Optional)

For production, consider using environment variables for authentication:

```python
import os

USERS = {
    "admin": os.getenv("ADMIN_PASSWORD", "admin123"),
    "analyst": os.getenv("ANALYST_PASSWORD", "analyst456"),
    "viewer": os.getenv("VIEWER_PASSWORD", "viewer789")
}
```

---

## Quick Start Recommendation

**For immediate deployment**: Use **Streamlit Cloud**
1. Push your code to GitHub
2. Deploy on share.streamlit.io
3. Share the URL with your team

**For production use**: Use **Railway** or **DigitalOcean**
- Better performance
- Custom domains
- More control over environment

---

## Troubleshooting

### Common Issues:

1. **Large file size**: If Excel file is too large for free tiers
   - Compress the file
   - Consider loading from cloud storage

2. **Memory issues**: 
   - Optimize data loading
   - Use data sampling for large datasets

3. **Authentication**: 
   - Change default passwords before deployment
   - Consider implementing proper user management

### Support
- Streamlit Community: [discuss.streamlit.io](https://discuss.streamlit.io)
- Documentation: [docs.streamlit.io](https://docs.streamlit.io)

---

**Choose the option that best fits your needs and budget!** 🚀 