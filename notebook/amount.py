import os

def count_pdf_files(directory):
    # Check if directory exists
    if not os.path.isdir(directory):
        print("Error: Directory does not exist.")
        return -1
    
    # Initialize file count
    pdf_count = 0
    
    # Iterate through files in the directory
    for filename in os.listdir(directory):
        if filename.endswith(".pdf"):
            pdf_count += 1
    
    return pdf_count

if __name__ == "__main__":
    directory = "data/books"  # Specify the directory path directly as a string
    pdf_count = count_pdf_files(directory)
    
    if pdf_count >= 0:
        print(f"Number of PDF files in directory '{directory}': {pdf_count}")