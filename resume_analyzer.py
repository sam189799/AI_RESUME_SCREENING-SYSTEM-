def analyze_resume(resume_text):

    resume = resume_text.lower()

    suggestions = []
    strengths = []
    weaknesses = []

    # ---------- Strengths ----------
    if "python" in resume:
        strengths.append("Python Skill Found")

    if "sql" in resume:
        strengths.append("SQL Skill Found")

    if "machine learning" in resume:
        strengths.append("Machine Learning Knowledge")

    if "deep learning" in resume:
        strengths.append("Deep Learning Knowledge")

    if "project" in resume:
        strengths.append("Projects Included")

    if "intern" in resume:
        strengths.append("Internship Experience Found")

    if "github" in resume:
        strengths.append("GitHub Profile Available")

    if "linkedin" in resume:
        strengths.append("LinkedIn Profile Available")


    # ---------- Weaknesses ----------
    if "objective" not in resume:
        weaknesses.append("Career Objective section is missing.")

    if "certification" not in resume and "certificate" not in resume:
        weaknesses.append("Add relevant certifications.")

    if "achievement" not in resume:
        weaknesses.append("Include achievements or awards.")

    if "power bi" not in resume:
        weaknesses.append("Power BI skill is missing.")

    if "aws" not in resume:
        weaknesses.append("Cloud skills (AWS/Azure/GCP) are missing.")


    # ---------- Suggestions ----------
    if "github" not in resume:
        suggestions.append("Add your GitHub profile link.")

    if "linkedin" not in resume:
        suggestions.append("Add your LinkedIn profile.")

    if "tensorflow" not in resume:
        suggestions.append("Mention TensorFlow if you have worked with it.")

    if "tableau" not in resume:
        suggestions.append("Include Tableau or Power BI projects.")

    if "intern" not in resume:
        suggestions.append("Mention internship or practical experience.")

    if "communication" not in resume:
        suggestions.append("Mention communication and teamwork skills.")


    # ---------- Default Messages ----------
    if len(weaknesses) == 0:
        weaknesses.append("No major weaknesses detected.")

    if len(suggestions) == 0:
        suggestions.append(
            "Excellent resume! Keep updating it with new projects, certifications, and skills."
        )

    return suggestions, strengths, weaknesses