import re

# Skill-based ATS Matcher

def calculate_score(resume, jd):

    resume = resume.lower()
    jd = jd.lower()

    # Extract words
    resume_words = set(re.findall(r'\b[\w\+\#\.]+\b', resume))
    jd_words = set(re.findall(r'\b[\w\+\#\.]+\b', jd))

    # Common technical skills
    skills = [
        "python",
        "sql",
        "java",
        "c++",
        "html",
        "css",
        "javascript",
        "flask",
        "django",
        "pandas",
        "numpy",
        "tensorflow",
        "scikit-learn",
        "opencv",
        "machine",
        "learning",
        "deep",
        "data",
        "analysis",
        "statistics",
        "excel",
        "power",
        "bi",
        "tableau",
        "git",
        "github",
        "mongodb",
        "mysql",
        "api",
        "linux"
    ]

    matched = []
    missing = []

    for skill in skills:

        if skill in jd:

            if skill in resume:
                matched.append(skill)
            else:
                missing.append(skill)

    # ATS Score
    total = len(matched) + len(missing)

    if total == 0:
        score = 0
    else:
        score = round((len(matched) / total) * 100, 2)

    return score, matched, missing


def keyword_analysis(resume_text, jd):

       resume = resume_text.lower()
       jd = jd.lower()

def keyword_analysis(resume_text, jd):

    resume = resume_text.lower()
    jd = jd.lower()

    keywords = list(set(jd.split()))

    found = []
    missing = []

    for word in keywords:

        if len(word) < 3:
            continue

        if word in resume:
            found.append(word)
        else:
            missing.append(word)

    return found, missing