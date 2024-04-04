import torch
import time

# Hyperparameters
batch_size = 64
block_size = 256
max_iters = 5000
eval_interval = 500
learning_rate = 3e-4
device = 'cpu'
eval_iters = 200
n_embd = 384
n_head = 6
n_layer = 6
dropout = 0.2

# Calculate number of parameters
num_params = (n_embd * block_size * n_layer +
              n_embd * n_embd * 4 * n_head * n_layer +
              n_embd * block_size * 4 * n_head * n_layer +
              block_size * n_embd + n_embd +
              block_size * n_embd * 2 +
              block_size * 4 +
              n_embd * 2 +
              n_embd * 2 +
              2)

# Function to format large numbers
def format_large_number(num):
    if num < 1e3:
        return str(num)
    elif num < 1e6:
        return f"{num / 1e3:.1f} K"
    elif num < 1e9:
        return f"{num / 1e6:.1f} M"
    elif num < 1e12:
        return f"{num / 1e9:.1f} B"
    else:
        return str(num)

# Estimate time per iteration (in seconds)
time_per_iteration = 0.001 * num_params / batch_size

# Estimate total training time (in seconds)
total_training_time = max_iters * time_per_iteration

# Convert total training time to hours and minutes
hours = int(total_training_time // 3600)
minutes = int((total_training_time % 3600) // 60)
days = int(hours/ 24)
print(f"Number of Parameters: {format_large_number(num_params)}")
print(f"Estimated total training time:{days} days, {hours} hours, and {minutes} minutes")

