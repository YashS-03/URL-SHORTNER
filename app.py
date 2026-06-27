from flask import Flask, redirect, request, jsonify
from database import get_url
from url_shortener import shorten

app = Flask(__name__)

@app.route("/shorten", methods=["POST"])
def shorten_url():
    data = request.json
    long_url = data["url"]
    short_code = shorten(long_url)
    return jsonify({"short_code": short_code})

@app.route("/<short_code>")
def redirect_url(short_code):
    url = get_url(short_code)

    if url:
        return redirect(url[1], code = 301)
    
    return jsonify({"ERROR": "URL NOT FOUND !!!"}), 404

if __name__ == "__main__":
    app.run(debug=True)