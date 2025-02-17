from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/api")
def api():
    data = {
        "message": "Welcome to the Flask API",
        "status": "success"
    }
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)