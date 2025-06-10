from fastapi import APIRouter
from typing import List
from app.models import Project

router = APIRouter(prefix="/api/projects", tags=["projects"])

# Sample projects data
projects = [
    {
        "id": 1,
        "title": "Streams of Thoughts",
        "description": "A blog  website built with Flask  and modern web technologies like jinja2, html, css, javascript, bootstrap, sqlite3 showcasing crud operations , user authentication, and more",
        "technologies": ["Python", "Flask ", "HTML", "CSS", "JavaScript", "Jinja2", "SQLite3"],
        "image_url": "",
        "video_url": '/static/videos/flask_blog_video.mp4',
        "github_url": "https://github.com/nikhilgupta-dev-bit/streams-of-thoughts-",
        "project_url": None
    },
    {
        "id": 2,
        "title": "Expense Flow",
        "description": "A full-stack expense tracker showcasing crud operations , interative ui ,login and signup functionality,total expense by the user and catogarization  and chart visualization uisng chart.js and sqlite3",
        "technologies": ["Python", "Django", "Html", "PostgreSQL", "Bootstrap", "Chart.js", "Jinja2", "css"],
        "image_url": "/static/images/expense_tracker.png",
        "video_url": None,
        "github_url": "https://github.com/nikhilgupta-dev-bit/ExpenseFlow",
        "project_url": "https://media.licdn.com/dms/image/v2/D5622AQFCGi7J6VYceA/feedshare-shrink_2048_1536/B56ZcsfZevHUAw-/0/1748798118664?e=1752710400&v=beta&t=xbfUbCv64-TalCrs83dpLdXayh4aEte0QAkAo2wLeDM"
    },
    {
        "id": 3,
        "title": "Mood tunes",
        "description": "A full-stack music player showcasing crud operations , interative ui ,login and signup functionality,music player with playlist management and more,using emotional analysis and sentiment analysis(NLP) currently in working state ",
        "technologies": ["Python", "Django", "Html", "PostgreSQL", "Bootstrap", "Jinja2", "css", "javascript"],
        "image_url": "/static/images/moodtune.Ai..png",
        "video_url": '',
        "github_url": "https://github.com/nikhilgupta-dev-bit/moodtunes",
        "project_url": None
    },
    {
        "id": 4,
        "title": "Currency Converter",
        "description": "A full stack currency particular converter using api  and interative ui",
        "technologies": ["Python", "streamlit", "Html", "PostgreSQL", "Bootstrap", "Jinja2", "css", "javascript"],
        "image_url": "/static/images/currency_converter.png",
        "video_url": None,
        "github_url": "https://github.com/nikhilgupta-dev-bit/streamlit/blob/streamlit/currency_exchange.py",
        "project_url": None
    }
]

@router.get("/", response_model=List[Project])
async def get_projects():
    return projects 