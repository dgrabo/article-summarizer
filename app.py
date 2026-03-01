from flask import Flask

app = Flask(__name__)

@app.route("/")
def summarize_article():
    return "<h1>Article Summarizer</h1>" \
    "<button>Summarize</button> <br>" \
    "<input type=url placeholder name=username>" 



if __name__ == "__main__":
    app.run(debug=True)