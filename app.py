from flask import Flask, render_template, request
from summarizer import fetch_article, generate_summary

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/summarize", methods=["POST"])
def summarize():
    url = request.form.get("url", "").strip()

    if not url:
        return render_template("index.html", error="Please provide a URL.")

    try:
        text = fetch_article(url)
    except Exception:
        return render_template("index.html", error="Could not fetch the article. Please check the URL.")

    if not text:
        return render_template("index.html", error="Could not extract text from the article.")

    try:
        summary = generate_summary(text)
    except Exception:
        return render_template("index.html", error="Failed to generate summary. Please try again.")

    return render_template("index.html", summary=summary)


if __name__ == "__main__":
    app.run(debug=True)
