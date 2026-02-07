from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)

# Allow all origins, headers, and methods
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Backend running"})
@app.route("/generate-resume", methods=["POST", "OPTIONS"])
def generate_resume():
    # Handle preflight request
    if request.method == "OPTIONS":
        return jsonify({"status": "ok"}), 200

    data = request.json
    return jsonify({
        "status": "success",
        "received_data": data
    })


@app.route("/ats-score", methods=["POST", "OPTIONS"])
def ats_score():
    # Handle preflight request
    if request.method == "OPTIONS":
        return jsonify({"status": "ok"}), 200

    data = request.json

    resume_text = data.get("resume", "")
    job_description = data.get("jobDescription", "")

    score = min(100, max(50, len(resume_text) % 100))

    return jsonify({
        "ats_score": score,
        "missing_keywords": ["REST API", "Pandas", "Machine Learning"]
    })


if __name__ == "__main__":
    app.run(debug=True)
