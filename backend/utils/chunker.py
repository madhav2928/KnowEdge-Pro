import fitz  # PyMuPDF

def chunk_pdf(uploaded_file):
    doc = fitz.open(stream=uploaded_file.file.read(), filetype="pdf")
    chunks = []
    for page in doc:
        text = page.get_text()
        chunks.extend([text[i:i+500] for i in range(0, len(text), 500)])
    return chunks