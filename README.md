
🕷️ NewsCrawler — AI Powered News Intelligence Platform

NewsCrawler is a modern AI-powered news aggregation and summarization web application built using Streamlit. It collects real-time news from multiple sources, processes it, and uses a Large Language Model (Groq API) to generate concise, meaningful summaries.

The platform is designed to reduce information overload and help users consume news faster through AI-generated insights instead of long articles.

🚀 Features
🌐 Multi-Source News Aggregation
Fetches news from multiple RSS feeds across categories like Business, Sports, Technology, and General.
🤖 AI-Powered Summarization
Uses Groq LLM to convert long news articles into short, clear summaries.
⚡ Real-Time Updates
Auto-refresh system ensures the latest news is always available.
📊 Category-Based Filtering
Easily explore news by categories for better organization.
🧠 Smart Sorting System
Displays news in a structured format (Latest → Oldest).
🖥️ Interactive Dashboard
Built with Streamlit for a clean and responsive user experience.

🏗️ System Architecture

RSS Feeds → Data Extraction → Data Cleaning → AI Summarization → Streamlit UI Rendering

Each news article is processed through an AI layer that transforms raw content into structured insights.

🛠️ Tech Stack
Python — Core backend logic
Streamlit — Web UI framework
Feedparser — RSS feed scraping
Groq API (LLM) — AI-powered summarization
Datetime & Threading — Data handling & performance optimization


📁 Project Structure
NewsCrawler/
│
├── app.py              # Main Streamlit application
├── scraper.py          # RSS feed scraping logic
├── ai_summary.py       # AI summarization using Groq API
├── requirements.txt    # Project dependencies
└── README.md  

⚙️ Installation
1. Clone the repository
git clone https://github.com/your-username/newscrawler.git
cd newscrawler
2. Create virtual environment
python -m venv venv
venv\Scripts\activate   # Windows
# source venv/bin/activate   # Mac/Linux
3. Install dependencies
pip install -r requirements.txt
🔑 Environment Variables

Create a .env file in the root directory:

GROQ_API_KEY=your_api_key_here
▶️ Run the Application
streamlit run app.py

If Streamlit is not recognized:

python -m streamlit run app.py
🧠 How It Works
RSS feeds are collected from multiple sources
Articles are extracted and cleaned
Data is categorized and sorted by time
Groq LLM generates short AI summaries
Streamlit displays everything in an interactive dashboard
📌 Future Improvements
🔍 Smart keyword-based search
💾 Bookmark/save articles feature
📱 Mobile-friendly UI optimization
📊 Sentiment analysis of news
🌍 Integration with News APIs for wider coverage
👩‍💻 Author

Niharika Jaiswal

Focused on building projects in:

AI-powered applications
Python automation systems
Data-driven web apps
