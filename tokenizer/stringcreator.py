import os
import pdfplumber
import logging
import time
from multiprocessing import Pool, cpu_count

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def extract_text_from_pdf(pdf_file_path):
    """Extracts text from a single PDF file using pdfplumber."""
    text = ""
    try:
        with pdfplumber.open(pdf_file_path) as pdf:
            for page in pdf.pages:
                text += page.extract_text()
    except Exception as e:
        logger.error(f"An unexpected error occurred while reading {pdf_file_path}: {e}")
    return text

def extract_text_from_pdfs_parallel(pdf_file_paths):
    """Extracts text from multiple PDFs in parallel."""
    with Pool(cpu_count()) as pool:
        texts = pool.map(extract_text_from_pdf, pdf_file_paths)
    return ''.join(texts)

def save_text_to_file(text, output_file_path):
    """Saves the extracted text to a file."""
    try:
        with open(output_file_path, "w", encoding="utf-8") as file:
            file.write(text)
        logger.info(f"Text saved to {output_file_path}")
    except Exception as e:
        logger.error(f"An error occurred while saving the text to file: {e}")

if __name__ == '__main__':
    start_time = time.time()
    
    directory_path = r"C:\Users\rafa0\Desktop\pj\fuckgit\LAPLACE\data\books"
    output_directory = os.path.join(os.getcwd(), "saved_files")
    os.makedirs(output_directory, exist_ok=True)
    output_file_path = os.path.join(output_directory, "output.txt")

    # Check if the directory is accessible
    if not os.access(directory_path, os.R_OK):
        logger.error(f"Cannot read from directory: {directory_path}")
    else:
        # Extract text from PDFs
        pdf_file_paths = [os.path.join(directory_path, filename) for filename in os.listdir(directory_path) if filename.endswith(".pdf")]
        text_data = extract_text_from_pdfs_parallel(pdf_file_paths)

        # Save text to file
        save_text_to_file(text_data, output_file_path)

    end_time = time.time()
    execution_time = end_time - start_time
    logger.info(f"Execution time: {execution_time} seconds")
