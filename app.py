from flask import Flask, redirect, request, jsonify
from database import get_url, increment_clicks, get_all_urls, init_db
from url_shortener import shorten

app = Flask(__name__)

@app.route("/shorten", methods=["POST"])
def shorten_url():
    data = request.json
    long_url = data["url"]
   
    if not long_url.startswith(("http://", "https://")):
        return jsonify({"error": "Invalid URL"}), 400

    short_code = shorten(long_url)
    return jsonify({"short_code": short_code})

@app.route("/<short_code>")
def redirect_url(short_code):
    url = get_url(short_code)

    if url:
        increment_clicks(short_code)
        return redirect(url[1], code = 301)

    return jsonify({"ERROR": "URL NOT FOUND !!!"}), 404

@app.route("/dashboard")
def dashboard():
    urls = get_all_urls()

    html = "<table border='1'><tr><th>Short Code</th><th>Original URL</th><th>Clicks</th></tr>"
    
    for row in urls:
        html += f"<tr><td>{row[2]}</td><td>{row[1]}</td><td>{row[3]}</td></tr>"
    
    html += "</table>"
    return html

init_db()
if __name__ == "__main__":
    app.run(debug=False)