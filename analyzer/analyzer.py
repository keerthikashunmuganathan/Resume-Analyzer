from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import spacy

nlp = spacy.load("en_core_web_sm")

def analyze_resume(resume_text, job_desccription):
    vecctorize = TfidfVectorizer()
    tfidf_matrix = vecctorize.fit_transform([resume_text, job_desccription])

    similarity_score = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]
    score_percentage = round(similarity_score*100, 2)

    jd_tokens = set(job_desccription.lower().split())
    resume_tokens = set(resume_text.lower().split())
    missing_keywords = list(jd_tokens-resume_tokens)

    return {
        "match_score" : score_percentage,
        "missing_keywords" : missing_keywords[:10]
    }