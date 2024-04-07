import os

# Directory containing the files
directory_path = r"C:\Users\rafa0\Desktop\pj\laplace\LAPLACE\data\saved"

# Number of files to process
num_files_to_process = 5  # Change this to the desired number of files

# Initialize an empty string to store the text content
text = ""

# Counter to keep track of the number of files processed
files_processed = 0

# Loop through all files in the specified directory
for filename in os.listdir(directory_path):
    if filename.endswith(".txt"):
        file_path = os.path.join(directory_path, filename)
        
        # Read the content of each .txt file and append it to the 'text' variable
        with open(file_path, 'r', encoding='utf-8') as file:
            text += file.read()
        
        # Increment the counter
        files_processed += 1
        
        # Break the loop if the desired number of files has been processed
        if files_processed == num_files_to_process:
            break

# Convert the text to bytes and then to a list of integers
tokens = list(text.encode("utf-8"))

# Build the token to index mapping
unique_tokens = set(tokens)
token_to_idx = {token: i for i, token in enumerate(unique_tokens)}

# Merge the tokens and build the merges dictionary
print("Merging tokens...")
merges = {}
for i in range(256, 276):
    pair = (i - 256, i - 256 + 1)
    print(f"merging {pair} into a new token {i}")
    new_tokens = []
    i = 0
    while i < len(tokens):
        if i < len(tokens) - 1 and tokens[i] == pair[0] and tokens[i+1] == pair[1]:
            new_tokens.append(i)
            i += 2
        else:
            new_tokens.append(tokens[i])
            i += 1
    tokens = new_tokens
    merges[pair] = i

# Update the token_to_idx dictionary with the merged tokens
for pair, idx in merges.items():
    token_to_idx[idx] = idx

print("Tokens length:", len(tokens))
print("ids length:", len(tokens))
print(f"compression ratio: {len(text.encode('utf-8')) / len(tokens):.2f}X")

def decode(ids):
    tokens = b"".join(bytes([idx]) for idx in ids)
    text = tokens.decode("utf-8", errors="replace")
    return text

def encode(text):
    tokens = list(text.encode("utf-8"))
    while len(tokens) >= 2:
        stats = get_stats(tokens)
        pair = min(stats, key=lambda p: merges.get(p, float("inf")))
        if pair not in merges:
            break
        idx = merges[pair]
        tokens = merge(tokens, pair, idx)
    return tokens

def get_stats(ids):
    counts = {}
    for pair in zip(ids, ids[1:]):
        counts[pair] = counts.get(pair, 0) + 1
    return counts

def merge(ids, pair, idx):
    new_ids = []
    i = 0
    while i < len(ids):
        if i < len(ids) - 1 and ids[i] == pair[0] and ids[i+1] == pair[1]:
            new_ids.append(idx)
            i += 2
        else:
            new_ids.append(ids[i])
            i += 1
    return new_ids

print(decode([128]))
print(encode(""))