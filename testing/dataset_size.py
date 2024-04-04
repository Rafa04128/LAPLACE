def calculate_data_size(model_size_millions, average_tokens_per_example, total_examples):
    """
    Calculate the estimated size of text data needed to train a language model.

    Parameters:
        model_size_millions (float): Number of parameters in the language model (in millions).
        average_tokens_per_example (int): Average number of tokens per example.
        total_examples (int): Total number of examples needed to train the model.

    Returns:
        float: Estimated size of text data in gigabytes.
    """
    model_size = model_size_millions * 1e6  # Convert to total number of parameters
    total_tokens = average_tokens_per_example * total_examples
    # Assume each token occupies 4 bytes (a typical assumption for Unicode text)
    bytes_per_token = 4
    total_bytes = total_tokens * bytes_per_token
    # Convert bytes to gigabytes
    data_size_gb = total_bytes / (1024**3)
    return data_size_gb

# Hyperparameters
model_size_millions = 36.3  # Number of parameters in the language model (in millions)
average_tokens_per_example = 256  # Average number of tokens per example
total_examples = 1e9  # Total number of examples needed to train the model

# Calculate data size
data_size_gb = calculate_data_size(model_size_millions, average_tokens_per_example, total_examples)
print(f"Estimated size of text data needed: {data_size_gb:.2f} GB")
