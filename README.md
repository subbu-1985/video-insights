# 🎬 Video Insights Detection AI

> An intelligent AI-powered video analysis platform built with Django, Google Gemini AI, and Claude Sonnet. Upload any video and instantly get transcripts, summaries, keywords, object detection, key moments, engagement analytics, ML model analysis, and an interactive AI chatbot — all in one futuristic sci-fi dashboard.

---

## 🧠 AI & Tech Stack

| Layer | Technology | Purpose |
|---|---|---|
| Backend Framework | Django 5.x (Python 3.10) | Web application & routing |
| Primary AI | Google Gemini (gemini-3-flash-preview) | Video analysis, transcription, summarization |
| Chatbot AI | Claude Sonnet via OpenRouter | Neural Chat Q&A over video content |
| Object Detection | YOLOv8 (Ultralytics) | Human presence & activity detection |
| Face Detection | Haar Cascade (OpenCV) | Face detection in video frames |
| Keyword Extraction | KeyBERT + Sentence Transformers | Engagement scoring from transcript |
| Database | SQLite | Data persistence |
| Frontend | HTML5, CSS3, JavaScript, Orbitron Font | Sci-fi themed UI |
| Email Service | Gmail SMTP | OTP verification & password reset |
| PDF Export | ReportLab | Downloadable insights report |

---

## ✨ Features

- 🎥 **Video Upload** — MP4 file upload (up to 90MB) or YouTube URL
- 📝 **AI Transcript** — Full speech-to-text extraction via Gemini
- 📋 **Auto Summary** — Two-sentence AI-generated video summary
- 🏷️ **Keyword Extraction** — Topic-relevant hashtags via Gemini + KeyBERT
- 👁️ **Object Detection** — Visual objects identified by Gemini vision
- 👤 **Human Presence Detection** — YOLOv8 detects people in video frames
- 😊 **Face Detection** — Haar Cascade detects faces across frames
- ⏱️ **Key Moments Timeline** — Real timestamps with event descriptions
- 📊 **Engagement Wave** — Segment-level engagement scoring via KeyBERT
- 🎙️ **Speech vs Silence** — Audio ratio analytics
- 🤖 **Neural Chat** — Claude Sonnet-powered chatbot for video Q&A
- 💬 **Chat History** — View all past conversations per video
- 📄 **PDF Export** — Full insights report including ML results and chat history
- 🔐 **OTP Verification** — Email-based account activation (6-digit code, 10-min expiry)
- 🔑 **Password Reset** — Secure HTML email with tokenized reset link
- 👤 **Admin Panel** — User management, activation, and analytics dashboard
- 📈 **Engagement Hub** — Aggregated analytics across all user videos

---

## 🚀 Project Setup

### Prerequisites

Make sure you have the following installed on your system:
- Python 3.10+
- pip
- Git

---

### 1. Clone the Repository



---

### 2. Create and Activate Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate — Windows
venv\Scripts\activate

# Activate — Mac / Linux
source venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

If `requirements.txt` is not present, install manually:

```bash
pip install django
pip install google-generativeai
pip install python-dotenv
pip install reportlab
pip install opencv-python
pip install ultralytics
pip install keybert
pip install sentence-transformers
pip install yt-dlp
pip install requests
```

---

### 4. Create Environment File

Create a `.env` file in the **root directory** of the project:

```env
SECRET_KEY=your_django_secret_key_here
GEMINI_API_KEY=your_gemini_api_key_here
OPENROUTER_API_KEY=your_openrouter_api_key_here
EMAIL_HOST_USER=your_gmail_address@gmail.com
EMAIL_HOST_PASSWORD=your_gmail_app_password_here
```

#### How to get each key:

**Django Secret Key:**
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

**Gemini API Key:**
- Visit https://aistudio.google.com/app/apikey
- Click **Create API Key**
- Copy and paste into `.env`
- Free tier: gemini-3-flash-preview

**OpenRouter API Key (for Claude Sonnet chatbot):**
- Visit https://openrouter.ai/
- Sign up and go to **API Keys**
- Create a new key and paste into `.env`

**Gmail App Password:**
- Go to Google Account → Security → 2-Step Verification → App Passwords
- Generate a password for **Mail**
- Use the 16-character app password (NOT your regular Gmail password)

---

### 5. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

### 6. Fix the Site Domain (Required for password reset emails)

```bash
python manage.py shell
```

```python
from django.contrib.sites.models import Site
site = Site.objects.get(id=1)
site.domain = '127.0.0.1:8000'
site.name = 'VideoInsights'
site.save()
exit()
```

---

### 7. Create Superuser (Admin Account)

```bash
python manage.py createsuperuser
```

Enter your email and password when prompted.

---

### 8. Run the Development Server

```bash
python manage.py runserver
```

Open your browser and visit:
```
http://127.0.0.1:8000
```

---

## 📁 Project Structure

```
Video-Insights-Detection/
│
├── accounts/               # Authentication module
│   ├── models.py           # User, EmailOTP, Notification models
│   ├── views.py            # Login, signup, OTP, password reset views
│   ├── urls.py
│   └── admin.py
│
├── videos/                 # Video management module
│   ├── models.py           # VideoAnalysis model
│   ├── views.py            # Upload, list, delete, PDF download, engagement hub
│   ├── ml_analyzer.py      # YOLOv8 + Haar Cascade + KeyBERT ML pipeline
│   ├── utils.py            # YouTube downloader, Gemini API helper
│   └── urls.py
│
├── analysis/               # AI processing module
│   ├── views.py            # Gemini API integration & insight rendering
│   └── urls.py
│
├── chatbot/                # Neural Chat module
│   ├── models.py           # ChatMessage model
│   ├── views.py            # Claude Sonnet chat & history views
│   └── urls.py
│
├── core/                   # Project configuration
│   ├── settings.py         # Django settings
│   └── urls.py             # Root URL routing
│
├── templates/              # All HTML templates
├── static/                 # CSS, JS, static assets
├── media/                  # Uploaded video files (auto-created)
├── .env                    # Environment variables — DO NOT commit to Git
├── .gitignore
├── db.sqlite3              # SQLite database (auto-created after migrate)
└── manage.py
```

---

## 🗄️ Database Tables

The project uses **SQLite** — no configuration required. The `db.sqlite3` file is created automatically when you run migrations.

| Table | App | Description |
|---|---|---|
| `accounts_user` | accounts | Custom user accounts with email login |
| `accounts_emailotp` | accounts | 6-digit OTP codes with 10-min expiry |
| `accounts_notification` | accounts | User notification messages |
| `videos_videoanalysis` | videos | All video metadata and AI/ML results |
| `chatbot_chatmessage` | chatbot | Chat history per video per user |

To view the database visually, open `db.sqlite3` with [DB Browser for SQLite](https://sqlitebrowser.org/) — a free GUI tool.

---

## 🤖 AI Pipeline Overview

```
Video Uploaded
      ↓
Gemini API (gemini-3-flash-preview)
→ Transcript, Summary, Keywords, Objects, Key Moments, Activity Type
      ↓
Local ML Models
→ YOLOv8: Human presence detection
→ Haar Cascade: Face detection
→ KeyBERT + Sentence Transformers: Engagement scoring
      ↓
Results saved to SQLite Database
      ↓
Dashboard renders all insights
      ↓
Claude Sonnet (via OpenRouter)
→ Answers user questions using stored insights as context
```

---


### ❌ Password reset link opens `example.com`
```bash
python manage.py shell
```
```python
from django.contrib.sites.models import Site
site = Site.objects.get(id=1)
site.domain = '127.0.0.1:8000'
site.save()
exit()
```


## ⚙️ Environment Variables Reference

| Variable | Description |
|---|---|
| `SECRET_KEY` | Django secret key for cryptographic signing |
| `GEMINI_API_KEY` | Google Gemini API key for video analysis |
| `OPENROUTER_API_KEY` | OpenRouter key for Claude Sonnet chatbot |
| `EMAIL_HOST_USER` | Gmail address used to send emails |
| `EMAIL_HOST_PASSWORD` | Gmail App Password (16 characters) |

> ⚠️ Never commit your `.env` file to Git. Make sure `.env` is listed in your `.gitignore`.

---

## 📄 License

This project is developed for **academic and educational purposes** as part of a B.Tech Computer Science & Engineering major project submission.

> *"Turning raw video into structured intelligence."*
