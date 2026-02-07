from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def calculate_ats_score(resume_text, job_description):
    documents = [resume_text, job_description]

    vectorizer = TfidfVectorizer(stop_words="english")
    tfidf_matrix = vectorizer.fit_transform(documents)

    similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]
    ats_score = round(similarity * 100, 2)

    resume_words = set(resume_text.lower().split())
    jd_words = set(job_description.lower().split())

    missing_keywords = list(jd_words - resume_words)
    missing_keywords = missing_keywords[:10]  # limit output

    return ats_score, missing_keywords
