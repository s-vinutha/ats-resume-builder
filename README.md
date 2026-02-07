# ATS Resume Builder 🚀

A full-stack ATS-friendly resume builder that generates optimized resumes and evaluates resume compatibility against job descriptions using NLP.

## 🔧 Tech Stack
- Frontend: React (Vite)
- Backend: Flask
- NLP: TF-IDF, Cosine Similarity (scikit-learn)
- PDF: ReportLab

## ✨ Features
- ATS-compliant resume PDF generation
- Real-time ATS score calculation
- Keyword gap analysis
- Clean one-column resume format

## 🧠 How ATS Score Works
Resume and job description are vectorized using TF-IDF.  
Cosine similarity is calculated and scaled to generate an ATS score.

## ▶️ Run Locally

### Backend
```bash
cd backend
venv\Scripts\activate
python app.py


Version 2 – Enhanced with ATS scoring, multiple templates, and upcoming AI features.
