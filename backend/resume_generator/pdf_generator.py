from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

def generate_resume_pdf(data, file_path):
    c = canvas.Canvas(file_path, pagesize=A4)
    width, height = A4

    x = 40
    y = height - 40

    def draw(text):
        nonlocal y
        c.drawString(x, y, text)
        y -= 14

    # HEADER
    draw(data.get("name", "").upper())
    draw(f"Email: {data.get('email','')} | Phone: {data.get('phone','')}")
    y -= 20

    # SUMMARY
    draw("PROFESSIONAL SUMMARY")
    draw("Computer Science student with strong foundation in Python, data structures, and software development.")
    y -= 20

    # SKILLS
    draw("SKILLS")
    for skill in data.get("skills", "").split(","):
        draw(f"- {skill.strip()}")
    y -= 20

    # EDUCATION
    draw("EDUCATION")
    draw(data.get("education", ""))
    y -= 20

    # PROJECTS
    draw("PROJECTS")
    draw(data.get("projects", ""))
    y -= 20

    # EXPERIENCE
    draw("EXPERIENCE")
    draw(data.get("experience", ""))

    c.save()
