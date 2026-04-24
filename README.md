# Article Summarizer

A web app that takes a news article URL and returns a one-sentence AI-generated summary.

**Live Demo:** [AI Article Summarizer](https://article-summarizer-lemon-nine.vercel.app/)

## Tech Stack

- **Flask** — Web framework
- **newspaper3k** — Article extraction from URLs
- **Groq API** — AI summarization (Llama 3.3 70B)

## Setup

1. **Clone the repo**
   ```bash
   git clone https://github.com/dgrabo/article-summarizer.git
   cd article-summarizer
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate        # Mac/Linux
   venv\Scripts\activate           # Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Add your API key**

   Create a `.env` file in the root directory:
   ```
   GROQ_API_KEY=your-api-key-here
   ```
   Get a free API key at [console.groq.com](https://console.groq.com).

5. **Run the app**
   ```bash
   python app.py
   ```

6. Open `http://localhost:5000` in your browser.

## Usage

1. Paste a news article URL into the input field.
2. Click **Summarize**.
3. Get a one-sentence summary of the article.
