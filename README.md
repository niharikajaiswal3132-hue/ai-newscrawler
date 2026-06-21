NewsCrawler — AI-Powered Multi-Source News Intelligence Platform

NewsCrawler is a modern AI-powered news aggregation and summarization system built with Streamlit. It collects real-time news from multiple sources, organizes them intelligently, and uses a Large Language Model (Groq API) to generate concise, meaningful summaries.

The goal of this project is to reduce information overload and help users consume news faster with AI-driven insights instead of raw articles.

✨ Key Features
🌐 Multi-source News Aggregation
Fetches news from multiple RSS feeds across categories like Business, Sports, Technology, and General.
🤖 AI-Powered Summarization
Uses Groq LLM to convert long news articles into short, meaningful summaries.
⚡ Real-Time Updates
Auto-refresh system ensures the latest news is always available.
📊 Category-Based Filtering
Easily browse news by category for better organization.
🧠 Smart Sorting System
Articles are displayed in a structured order (Latest → Oldest) to maintain relevance.
🖥️ Interactive Streamlit Dashboard
Clean, responsive UI for smooth user experience.
🏗️ Architecture Overview

NewsCrawler follows a simple yet scalable pipeline:

RSS Feeds → Data Extraction → Cleaning & Structuring → AI Summarization → UI Rendering

Each article passes through an AI layer that transforms raw content into readable insights.

🛠️ Tech Stack
Technology	Purpose
Python	Core backend logic
Streamlit	Web application UI
Feedparser	RSS feed scraping
Groq API (LLM)	AI-based summarization
Datetime	Time-based sorting
Threading	Performance optimization

📁 Project Structure
NewsCrawler/
│
├── app.py              # Main Streamlit application
├── scraper.py          # Handles RSS feed extraction
├── ai_summary.py       # Groq AI summarization logic
├── requirements.txt    # Dependencies
└── README.md           # Project documentation

⚙️ Installation & Setup
1. Clone the repository
git clone https://github.com/your-username/newscrawler.git
cd newscrawler
2. Create virtual environment
python -m venv venv
venv\Scripts\activate   # Windows
# source venv/bin/activate   # macOS/Linux
3. Install dependencies
pip install -r requirements.txt
🔑 Environment Configuration

Create a .env file in the root directory:

GROQ_API_KEY=your_api_key_here
▶️ Running the Application
streamlit run app.py

If Streamlit is not recognized:

python -m streamlit run app.py
🧠 How It Works
The system fetches news from multiple RSS feeds
Articles are parsed and cleaned for consistency
Data is categorized and sorted by timestamp
Each article is processed using Groq LLM for summarization
Streamlit renders a structured, interactive dashboard
📌 Future Improvements
🔍 Keyword-based smart search engine
🧾 Save & bookmark feature for articles
📱 Mobile-optimized UI
📊 Sentiment analysis for news classification
🌍 Integration with APIs like NewsAPI for broader coverage
👨‍💻 Author

Niharika Jaiswal
Aspiring Software Developer focused on:

AI-integrated applications
Data-driven systems
Scalable Python projects
⭐ Project Purpose

This project was built to demonstrate practical skills in:

Web scraping & data engineering
AI integration using LLMs
Real-time dashboard development
Clean backend-to-frontend pipeline design

