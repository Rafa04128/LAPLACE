import os
import PyPDF2
import logging
import time
from concurrent.futures import ProcessPoolExecutor, as_completed
import cProfile

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def extract_text_from_pdfs(pdf_file_paths):
    """Extracts text from a list of PDF files using PyPDF2."""
    texts = []
    for pdf_file_path in pdf_file_paths:
        text = ""
        try:
            with open(pdf_file_path, 'rb') as file:
                pdf_reader = PyPDF2.PdfReader(file)
                for page in range(len(pdf_reader.pages)):
                    text += pdf_reader.pages[page].extract_text()
        except Exception as e:
            logger.error(f"An unexpected error occurred while reading {pdf_file_path}: {e}")
        texts.append(text)
    return texts

def save_text_to_file(text_data, output_file_path):
    """Saves the extracted text to a file."""
    try:
        with open(output_file_path, "w", encoding="utf-8") as file:
            file.write(text_data)
        logger.info(f"Text saved to {output_file_path}")
    except Exception as e:
        logger.error(f"An error occurred while saving the text to file: {e}")

def main():
    start_time = time.time()
    directory_path = r"C:\Users\rafa0\Desktop\pj\laplace\LAPLACE\data\books"
    output_directory = os.path.join(os.getcwd(), "saved_files")
    os.makedirs(output_directory, exist_ok=True)
    output_file_path = os.path.join(output_directory, "output.txt")

    # Check if the directory is accessible
    if not os.access(directory_path, os.R_OK):
        logger.error(f"Cannot read from directory: {directory_path}")
        exit(1)

    # Extract text from PDFs
    pdf_file_paths = [os.path.join(directory_path, filename) for filename in os.listdir(directory_path) if filename.endswith(".pdf")]
    batch_size = 4  # Adjust the batch size as needed
    with ProcessPoolExecutor() as executor:
        futures = []
        for i in range(0, len(pdf_file_paths), batch_size):
            batch = pdf_file_paths[i:i+batch_size]
            futures.append(executor.submit(extract_text_from_pdfs, batch))

        texts = []
        for future in as_completed(futures):
            texts.extend(future.result())

    # Combine extracted text from all files
    text_data = ''.join(texts)

    # Save text to file
    save_text_to_file(text_data, output_file_path)

    end_time = time.time()
    execution_time = end_time - start_time
    logger.info(f"Execution time: {execution_time} seconds")

if __name__ == '__main__':
    cProfile.run('main()', sort='cumtime')