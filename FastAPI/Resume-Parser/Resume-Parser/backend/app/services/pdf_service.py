import logging
from pypdf import PdfReader
logger = logging.getLogger("PDF")

def extract_text_from_pdf(file_path: str):
    logger.info("Starting PDF extraction")
    reader = PdfReader(file_path)
    page_count = len(reader.pages)
    logger.info(f"Pages detected: {page_count}")
    text = ""

    for page_number, page in enumerate(reader.pages,start=1):
        logger.info(f"Extracting page {page_number}/{page_count}")

        page_text = page.extract_text()
        if page_text:
            text += page_text
            text += "\n"

    logger.info(f"PDF extraction completed |chars={len(text)}")
    return text, page_count