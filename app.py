import streamlit as st
import feedparser
from datetime import datetime
import random
import time

from groq import Groq
client = Groq(api_key=st.secrets["GROQ_API_KEY"])
# ============================================================
# ⚙️ PAGE CONFIG
# ============================================================
st.set_page_config(
    page_title="NewsCrawler",
    page_icon="🕷️",
    layout="wide"
)

# ============================================================
# 🕷️ LOGO + TAGLINE
# ============================================================
try:
    st.sidebar.image("newscrawler_logo.png", use_container_width=True)
except:
    st.sidebar.markdown("## 🕷️ NewsCrawler")

st.sidebar.markdown("""
<div style="text-align:center; color:gray; font-size:13px; margin-top:6px;">
    📡 Real-time News Dashboard
</div>
""", unsafe_allow_html=True)

st.sidebar.markdown("---")

# ============================================================
refresh_time = st.sidebar.selectbox(
    "🔄 Auto Refresh (seconds)",
    [0, 10, 30, 60],
    index=0
)
if refresh_time != 0:
    time.sleep(refresh_time)
    st.rerun()

# ============================================================
# 🌗 THEME
# ============================================================
theme = st.sidebar.selectbox("🌓 Theme", ["Light", "Dark"])

if theme == "Dark":
    st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: white; }
    .stTextInput input, .stSelectbox, .stRadio { color: white !important; }
    </style>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
    <style>
    .stApp { background-color: white; color: black; }
    .stTextInput input, .stSelectbox, .stRadio { color: black !important; }
    </style>
    """, unsafe_allow_html=True)

# ============================================================
# 📰 RSS SOURCES
# ============================================================
RSS_FEEDS = {
    "Google News":   "https://news.google.com/rss",
    "BBC World":     "http://feeds.bbci.co.uk/news/world/rss.xml",
    "BBC Tech":      "http://feeds.bbci.co.uk/news/technology/rss.xml",
    "Yahoo Finance": "https://finance.yahoo.com/rss/topfinstories",
    "Al Jazeera":    "https://www.aljazeera.com/xml/rss/all.xml",
    "NPR News":      "https://feeds.npr.org/1001/rss.xml",
}

# ============================================================
# 🧠 CATEGORY ENGINE
# ============================================================
def get_category(title):
    t = title.lower()

    tech = ["tech", "ai", "software", "app", "startup", "google", "microsoft", "openai"]
    business = ["business", "market", "stock", "economy", "finance", "shares", "profit"]
    sports = ["cricket", "football", "match", "ipl", "fifa", "tournament"]
    politics = ["election", "government", "minister", "policy", "politics"]

    if any(x in t for x in tech):
        return "Tech"
    elif any(x in t for x in business):
        return "Business"
    elif any(x in t for x in sports):
        return "Sports"
    elif any(x in t for x in politics):
        return "Politics"
    else:
        return "World"

# ============================================================
# from groq import Groq

client = Groq(api_key=st.secrets["GROQ_API_KEY"])
def ai_summary(title):
    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{
                "role": "user",
                "content": f"Summarize this news headline in 2 bullet points:\n{title}"
            }],
            temperature=0.3
        )

        return response.choices[0].message.content

    except Exception as e:
        return "Summary unavailable"

# ============================================================
# 📅 DATE PARSER
# ============================================================
def parse_date(entry):
    try:
        if entry.get("published_parsed"):
            return datetime(*entry.published_parsed[:6])
        return datetime.min
    except:
        return datetime.min

# ============================================================
# 🚀 FETCH NEWS (FIXED & STABLE)
# ============================================================
@st.cache_data(ttl=300)
def get_news():
    all_news = []

    for source, url in RSS_FEEDS.items():
        try:
            feed = feedparser.parse(url)

            if not feed.entries:
                continue

            for entry in feed.entries:
                title = entry.get("title", "").strip()
                link = entry.get("link", "#")

                if not title:
                    continue

                all_news.append({
                    "title": title,
                    "summary": None,
                    "link": link,
                    "source": source,
                    "category": get_category(title),
                    "date": parse_date(entry)
                })

        except Exception:
            continue

    return all_news

# ============================================================
# 📰 TITLE
# ============================================================
st.title("🕷️ NewsCrawler - Real-Time News Dashboard")

# ============================================================
# 📥 LOAD NEWS
# ============================================================
news_list = get_news()

# ============================================================
# 🔍 FILTERS
# ============================================================
st.sidebar.header("Filters")

search = st.sidebar.text_input("🔍 Search")
source_filter = st.sidebar.selectbox("Source", ["All"] + list(RSS_FEEDS.keys()))
category_filter = st.sidebar.selectbox(
    "Category",
    ["All", "Tech", "Business", "Sports", "Politics", "World"]
)

sort_order = st.sidebar.radio(
    "📅 Sort",
    ["Latest → Oldest", "Oldest → Latest"]
)

# ============================================================
# 🔎 FILTER LOGIC
# ============================================================
filtered_news = []

for news in news_list:

    if search and search.lower() not in news["title"].lower():
        continue

    if source_filter != "All" and news["source"] != source_filter:
        continue

    if category_filter != "All" and news["category"] != category_filter:
        continue

    filtered_news.append(news)

# ============================================================

# ============================================================
# 📅 SORTING
# ============================================================
filtered_news.sort(
    key=lambda x: x["date"],
    reverse=(sort_order == "Latest → Oldest")
)
# ============================================================




 # 📰 DISPLAY (CLIENT READY VERSION)
# ============================================================

if not filtered_news:
    st.warning("No news found.")

else:
    for news in filtered_news:
        with st.container():

            title = news["title"]

            # HEADLINE
            st.markdown(f"### 📰 {title}")

            # BADGES ROW
            col1, col2 = st.columns([1, 4])

            

            # META INFO
            st.markdown(
                f"**Source:** {news['source']} | **Category:** {news['category']}"
            )

            st.markdown(f"📅 **Date:** {news['date']}")

            st.markdown(f"[🔗 Read Full Article]({news['link']})")

            # AI SUMMARY (ON DEMAND - FAST)
            if st.button("🧠 Generate AI Summary", key=title):
                with st.spinner("Generating AI insight..."):
                    summary = ai_summary(title)
                    st.info(summary)

            st.divider()


            
