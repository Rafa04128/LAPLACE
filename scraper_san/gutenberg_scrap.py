import os
import requests
from bs4 import BeautifulSoup
import time

def sanitize_filename(title):
    # Remove invalid file name characters and whitespace characters
    invalid_chars = '<>:"/\\|?*\n\r'
    for char in invalid_chars:
        title = title.replace(char, '')
    # Replace spaces with underscores for consistency
    title = title.replace(' ', '_')
    # Limit the length of the title to avoid filesystem errors
    return title[:200]

def download_gutenberg_books(bookshelf_urls):
    base_url = "https://www.gutenberg.org"
    download_directory = "gutenberg_books"

    # Create the directory if it does not exist
    if not os.path.exists(download_directory):
        os.makedirs(download_directory)

    total_size = 0
    total_books = 0
    downloaded_books = 0
    start_time = time.time()

    for bookshelf_url in bookshelf_urls:
        try:
            # Fetch the content of the bookshelf page
            response = requests.get(bookshelf_url)
            soup = BeautifulSoup(response.content, 'html.parser')

            # Find all book list items
            book_list_items = soup.find_all('li', class_='booklink')

            print(f"Found {len(book_list_items)} books on {bookshelf_url}")

            # Iterate over each book list item
            for item in book_list_items:
                book_link = item.find('a')
                if book_link:
                    book_title = book_link.get_text().strip()
                    sanitized_title = sanitize_filename(book_title)
                    print(f"Located book: {book_title}")

                    book_page_url = base_url + book_link['href']
                    book_page_response = requests.get(book_page_url)
                    book_page_soup = BeautifulSoup(book_page_response.content, 'html.parser')

                    # Find the Plain Text UTF-8 download link
                    plain_text_link = book_page_soup.find('a', string='Plain Text UTF-8')
                    if plain_text_link:
                        plain_text_url = base_url + plain_text_link['href']
                        plain_text_response = requests.get(plain_text_url)

                        # Extract the text content
                        text_content = plain_text_response.text

                        # Save the text content to a .txt file
                        file_name = sanitized_title + '.txt'
                        full_path = os.path.join(download_directory, file_name)
                        with open(full_path, 'w', encoding='utf-8') as file:
                            file.write(text_content)
                        print(f"Downloaded and saved '{book_title}' as '{file_name}'")
                        total_size += len(text_content)
                        downloaded_books += 1
                    else:
                        print(f"No Plain Text UTF-8 download link found for '{book_title}'")

        except Exception as e:
            print(f"Error during processing: {e}")

    end_time = time.time()
    execution_time = end_time - start_time

    print(f"Total books downloaded: {downloaded_books}")
    print(f"Total size of downloaded books: {total_size / (1024 * 1024):.2f} MB")
    print(f"Execution time: {execution_time:.2f} seconds")

if __name__ == "__main__":
    bookshelf_urls = [
        "https://www.gutenberg.org/ebooks/bookshelf/102", #mathematics
        "https://www.gutenberg.org/ebooks/bookshelf/201", #Biologia
        "https://www.gutenberg.org/ebooks/bookshelf/211", #quimica
        "https://www.gutenberg.org/ebooks/bookshelf/101", #Astronomia
        "https://www.gutenberg.org/ebooks/bookshelf/11", #arte
        "https://www.gutenberg.org/ebooks/bookshelf/8",   #Anthropology
        "https://www.gutenberg.org/ebooks/bookshelf/10", #Architecture
        "https://www.gutenberg.org/ebooks/bookshelf/420", #sauce
        "https://www.gutenberg.org/ebooks/bookshelf/8", #arqueologia
        "https://www.gutenberg.org/ebooks/bookshelf/227", #Geologia
        "https://www.gutenberg.org/ebooks/bookshelf/106", #ciencia
        "https://www.gutenberg.org/ebooks/bookshelf/256", #Mas ciencia
        "https://www.gutenberg.org/ebooks/bookshelf/143", #Tech
    ]
    download_gutenberg_books(bookshelf_urls)
