import re

def check_resume(resume_text):

    resume = resume_text.lower()

    checks = {
        "Email": bool(re.search(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", resume_text)),
        "Phone Number": bool(re.search(r"\d{10}", resume_text)),
        "Education": ("education" in resume or "b.tech" in resume or "bachelor" in resume),
        "Skills": ("skills" in resume),
        "Projects": ("project" in resume),
        "Internship": ("intern" in resume),
        "Certifications": ("certification" in resume or "certificate" in resume),
        "GitHub": ("github" in resume),
        "LinkedIn": ("linkedin" in resume)
    }

    completed = sum(checks.values())
    total = len(checks)

    percentage = round((completed / total) * 100)

    return checks, percentage