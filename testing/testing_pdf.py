import os
import logging
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def check_pdf_validity(directory_path):
    """Check the validity of PDF files in the specified directory."""
    for filename in os.listdir(directory_path):
        if filename.endswith(".pdf"):
            pdf_file_path = os.path.join(directory_path, filename)
            logger.info(f"Checking PDF file: {pdf_file_path}")
            try:
                with open(pdf_file_path, 'rb') as file:
                    parser = PDFParser(file)
                    document = PDFDocument(parser)
                    if document.is_extractable:
                        logger.info(f"PDF file '{pdf_file_path}' is valid and readable.")
                    else:
                        logger.error(f"PDF file '{pdf_file_path}' is not valid or readable.")
            except Exception as e:
                logger.error(f"An unexpected error occurred while checking PDF file '{pdf_file_path}': {e}")

def main():
    directory_path = r"C:\Users\rafa0\Desktop\pj\laplace\LAPLACE\data\books"
    # Check if the directory is accessible
    if not os.access(directory_path, os.R_OK):
        logger.error(f"Cannot read from directory: {directory_path}")
        exit(1)

    # Check validity of PDF files in the specified directory
    check_pdf_validity(directory_path)

if __name__ == '__main__':
    main()
