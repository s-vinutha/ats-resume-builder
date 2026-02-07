from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # allow React to talk to Flask

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Flask backend running"})

@app.route("/generate-resume", methods=["POST"])
def generate_resume():
    data = request.json
    return jsonify({
        "status": "success",
        "received_data": data
    })

if __name__ == "__main__":
    app.run(debug=True)
