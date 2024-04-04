Self made model entire process.


Current Param. 

![Cube](cube.jpeg)

# hyperparameters
batch_size = 64 # how many independent sequences will we process in parallel?
block_size = 256 # what is the maximum context length for predictions?
max_iters = 5000
eval_interval = 500
learning_rate = 3e-4
device = 'cuda' if torch.cuda.is_available() else 'cpu'
eval_iters = 200
n_embd = 384
n_head = 6
n_layer = 6
dropout = 0.2

Running in CPU. 


using the Nano GPT architecture we are goin to add the decoder block as to predict the next token on a sequence.

Needs done.

Model. 
Decoder Block.
Parameters tunning

Tokenizer
Upgrade tokenization process.
Image tokenization
Audio tokenization


Data
Calculate correct amount of data to be trained.
Get all sort of data for testing. 
Books, code, wikipedia and etc

Testing.
Understand the base model comming soon, to make a test enviroment that works, after that high pace updates. 


Current expected training time base on current hardware.

Number of Parameters: 36.3 M
Estimated total training time:32 days, 787 hours, and 15 minutes

This not good.(Also this was made from my work computer so its kind of cute, this time should be basically cut in half by running on my home computer.)

Can also be speed up by using CUDA... Thinking about it, waiting for ROCM to be up to date. 




