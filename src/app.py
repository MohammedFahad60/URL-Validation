from flask import Flask, request, render_template
from dfa_validator import validate_url

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    if request.method == "POST":
        url = request.form.get("url")
        result = "Valid URL" if validate_url(url) else "Invalid URL"
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
