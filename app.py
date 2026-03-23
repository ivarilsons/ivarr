from flask import Flask, send_from_directory, jsonify
import json

app = Flask(__name__)

@app.route("/")
def index():
    return send_from_directory(".", "index.html")

@app.route("/leaderboard")
def leaderboard():
    return send_from_directory(".", "leaderboard.html")

@app.route("/data")
def data():
    with open("students_data.json") as f:
        return jsonify(json.load(f))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
