import os
from flask import Flask, render_template, request
from dotenv import load_dotenv
from newspaper import Article, Config
from groq import Groq

load_dotenv()

app = Flask(__name__)
client = Groq(api_key=os.getenv("GROQ_API_KEY"))


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/summarize", methods=["POST"])
def summarize():
    url = request.form.get("url", "").strip()

    if not url:
        return render_template("index.html", error="Please provide a URL.")

    try:
        config = Config()
        config.browser_user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        article = Article(url, config=config)
        article.download()
        article.parse()
        text = article.text
    except Exception:
        return render_template("index.html", error="Could not fetch the article. Please check the URL.")

    if not text:
        return render_template("index.html", error="Could not extract text from the article.")

    try:
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
        summary = response.choices[0].message.content
    except Exception:
        return render_template("index.html", error="Failed to generate summary. Please try again.")

    return render_template("index.html", summary=summary)


if __name__ == "__main__":
    app.run(debug=True)

