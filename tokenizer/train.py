import os
import time
from dojo import BasicTokenizer, RegexTokenizer

import sys
sys.path.append("path/to/parent/directory")

def read_text_from_directory(directory_path):
    """
    Read text data from all text files in the specified directory
    and concatenate their contents.
    """
    text = ""
    for filename in os.listdir(directory_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(directory_path, filename)
            with open(file_path, "r", encoding="utf-8") as file:
                text += file.read()
    return text

# Specify the directory containing the text files for training
directory_path = r"C:\Users\rafa0\Desktop\pj\laplace\LAPLACE\data\saved"

# Read text from all text files in the directory
text = read_text_from_directory(directory_path)

# Create a directory for models, so we don't pollute the current directory
os.makedirs("models", exist_ok=True)

t0 = time.time()
for TokenizerClass, name in zip([BasicTokenizer, RegexTokenizer], ["basic", "regex"]):
    # Construct the Tokenizer object and kick off verbose training
    tokenizer = TokenizerClass()
    tokenizer.train(text, 512, verbose=True)
    # Write two files in the models directory: name.model and name.vocab
    prefix = os.path.join("models", name)
    tokenizer.save(prefix)
t1 = time.time()

print(f"Training took {t1 - t0:.2f} seconds")
