from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
        <head>
            <title>Hello World Demo</title>
        </head>
        <body>
            <h1>Hello, World!</h1>
            <p>This is a simple Python Flask demo page.</p>
        </body>
    </html>
    """

@app.route("/health")
def health():
    return {"status": "running"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
