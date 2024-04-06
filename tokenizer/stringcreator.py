import os
import logging
import time
from concurrent.futures import ProcessPoolExecutor, as_completed
from pdfminer.high_level import extract_text

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def extract_text_from_pdfs(pdf_file_paths):
    """Extracts text from a list of PDF files using pdfminer."""
    texts = []
    for pdf_file_path in pdf_file_paths:
        try:
            text = extract_text(pdf_file_path)
            if not text.strip():
                logger.warning(f"No text found in {pdf_file_path}")
            texts.append((os.path.splitext(os.path.basename(pdf_file_path))[0], text))
        except Exception as e:
            logger.error(f"An unexpected error occurred while reading {pdf_file_path}: {e}")
    return texts

def save_text_to_file(text_data, output_directory):
    """Saves the extracted text to individual files."""
    for filename, text in text_data:
        output_file_path = os.path.join(output_directory, f"{filename}.txt")
        try:
            with open(output_file_path, "w", encoding="utf-8") as file:
                file.write(text)
            logger.info(f"Text saved to {output_file_path}")
        except Exception as e:
            logger.error(f"An error occurred while saving the text to file {output_file_path}: {e}")

def main():
    start_time = time.time()
    directory_path = r"C:\Users\rafa0\Desktop\pj\laplace\LAPLACE\data\book"
    output_directory = os.path.join(os.getcwd(), "saved_files")
    os.makedirs(output_directory, exist_ok=True)

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

        text_data = []
        for future in as_completed(futures):
            try:
                text_data.extend(future.result())
            except Exception as e:
                logger.error(f"An error occurred while processing a batch of PDF files: {e}")

    # Save text to individual files
    save_text_to_file(text_data, output_directory)

    end_time = time.time()
    execution_time = end_time - start_time
    logger.info(f"Execution time: {execution_time} seconds")

if __name__ == '__main__':
    main()
