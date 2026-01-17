from PyPDF2 import PdfReader

def retrieve_from_pdf(query, pdf_path="data/Sustainability_Knowledge_Base.pdf"):
    reader = PdfReader(pdf_path)
    query_words = set(query.lower().split())

    chunks = []

    for page in reader.pages:
        text = page.extract_text()
        if not text:
            continue

        # chunk by paragraphs
        paragraphs = [p.strip() for p in text.split("\n") if len(p.strip()) > 50]

        for para in paragraphs:
            para_words = set(para.lower().split())
            score = len(query_words.intersection(para_words))

            if score > 0:
                chunks.append((score, para))

    # sort by relevance
    chunks.sort(key=lambda x: x[0], reverse=True)

    # return best chunk only
    return [chunks[0][1]] if chunks else []

