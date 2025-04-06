from pdfminer.high_level import extract_text

pdf_path = "data/owasp/OWASP_Code_Review_Guide_v2.pdf"
txt_path = "data/owasp/owasp_code_review.txt"

text = extract_text(pdf_path)
with open(txt_path, "w", encoding="utf-8") as f:
    f.write(text)

print(f"PDF converted to text: {txt_path}")