import os
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)

from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
from ats_analyzer.ats_score import calculate_ats_score
from resume_generator.pdf_generator import generate_resume_pdf

app = Flask(__name__)

# Allow all origins, headers, and methods
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Backend running"})

@app.route("/generate-resume", methods=["POST", "OPTIONS"])
def generate_resume():
    if request.method == "OPTIONS":
        return jsonify({"status": "ok"}), 200

    data = request.json
    template = data.get("template", "classic")

    file_path = "resume.pdf"

    generate_resume_pdf(data, file_path)

    return send_file(file_path, as_attachment=True)



@app.route("/ats-score", methods=["POST", "OPTIONS"])
def ats_score():
    if request.method == "OPTIONS":
        return jsonify({"status": "ok"}), 200

    data = request.json

    resume_text = data.get("resume", "")
    job_description = data.get("jobDescription", "")

    score, missing_keywords = calculate_ats_score(
        resume_text, job_description
    )

    return jsonify({
        "ats_score": score,
        "missing_keywords": missing_keywords
    })



if __name__ == "__main__":
    app.run(debug=True)
