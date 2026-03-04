import os
from newspaper import Article, Config
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def fetch_article(url):
    config = Config()
    config.browser_user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    article = Article(url, config=config)
    article.download()
    article.parse()
    return article.text


def generate_summary(text):
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        max_tokens=100,
        messages=[
            {
                "role": "user",
                "content": f"Summarize the following article in exactly one sentence:\n\n{text}",
            }
        ],
    )
    return response.choices[0].message.content
