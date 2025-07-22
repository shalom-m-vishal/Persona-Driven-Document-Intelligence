from PyPDF2 import PdfReader

def extract_sections_from_pdf(pdf_path):
    reader = PdfReader(pdf_path)
    sections = []
    for i, page in enumerate(reader.pages):
        text = page.extract_text()
        if not text:
            continue
        lines = text.strip().split('\n')
        title = lines[0] if lines else "Untitled Section"
        sections.append({
            "title": title.strip(),
            "text": text.strip(),
            "page": i + 1
        })
    return sections