from flask import Flask, render_template, request, send_file
import os

from utils.resume_parser import extract_text
from utils.matcher import calculate_score, keyword_analysis
from utils.resume_analyzer import analyze_resume
from utils.report_generator import generate_report
from utils.resume_checker import check_resume

app = Flask(__name__)

# Folders
UPLOAD_FOLDER = "resumes"
REPORT_FOLDER = "reports"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(REPORT_FOLDER, exist_ok=True)


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/upload', methods=['POST'])
def upload():

    # Get uploaded resume
    file = request.files['resume']

    # Get Job Description
    jd = request.form['job_description']

    if file.filename == "":
        return "No file selected"

    # Save Resume
    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    # Extract Resume Text
    resume_text = extract_text(filepath)

    # Resume Completeness
    checks, completeness = check_resume(resume_text)

    # ATS Score
    score, matched, missing = calculate_score(resume_text, jd)

    found_keywords, missing_keywords = keyword_analysis(
    resume_text,
    jd
    )

    # Resume Analysis
    suggestions, strengths, weaknesses = analyze_resume(resume_text)

    # ATS Score Breakdown
    skills_score = min(len(matched) * 10, 100)

    projects_score = 90 if "project" in resume_text.lower() else 50

    education_score = 95 if "b.tech" in resume_text.lower() else 70

    experience_score = 85 if "intern" in resume_text.lower() else 60

    # Feedback
    if score >= 80:
        feedback = "Excellent Match ✅"
    elif score >= 60:
        feedback = "Good Match 👍"
    elif score >= 40:
        feedback = "Average Match ⚠️"
    else:
        feedback = "Poor Match ❌"

    # Resume Rating
    if score >= 90:
        rating = "A+"
    elif score >= 80:
        rating = "A"
    elif score >= 70:
        rating = "B"
    elif score >= 50:
        rating = "C"
    else:
        rating = "D"

    # PDF Report Path
    report_filename = f"{os.path.splitext(file.filename)[0]}_Report.pdf"
    report_path = os.path.join(REPORT_FOLDER, report_filename)

    # Generate PDF
    generate_report(
        report_path,
        score,
        feedback,
        rating,
        matched,
        missing,
        strengths,
        weaknesses,
        suggestions
    )

    return render_template(
        "result.html",
        filename=file.filename,
        score=score,
        feedback=feedback,
        rating=rating,
        matched=matched,
        missing=missing,
        strengths=strengths,
        weaknesses=weaknesses,
        suggestions=suggestions,
        report_filename=report_filename,
        skills_score=skills_score,
        projects_score=projects_score,
        education_score=education_score,
        experience_score=experience_score,
        checks=checks,
        completeness=completeness,
        found_keywords=found_keywords,
        missing_keywords=missing_keywords,
       
    )


@app.route("/download/<filename>")
def download(filename):
    return send_file(
        os.path.join(REPORT_FOLDER, filename),
        as_attachment=True
    )


if __name__ == "__main__":
    app.run(debug=True)