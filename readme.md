# Self made model entire process.




![Cube](cube.jpeg)







#---------------------------------
# hyperparameters

- batch_size: 64 
- block_size: 256 
- max_iters: 5000
- eval_interval: 500
- learning_rate: 3e-4
- eval_iters: 200
- n_embd: 384
- n_head: 6
- n_layer: 6
- dropout: 0.2

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




I want to have a fully running General Pre-trained transformer that its the main goal. 
After that the Plan is to apply all the up to date inference, fine tunning and training methods. 
LORA, Tokenization using bit compresion, Multi Agent MOE Mixture of experts. 
Excited for the hardships of this path. 

I will focus on code while I work around the computational power required. 





To train with fear of overfitting 
Estimated size of text data needed: 953.67 GB



Corrently on tokenization step.

Thinbgs to do, fixed the gpt4 tokenizer.

on mrclean.ipyng code needs to add the special tokens to the beginning and end of documents for training purpose


Do later today. after F1 kekeke


HARDWARE

SAMSUNG 990 PRO 2TB

MSI GEFORCE RTX 4090 GAMING TRIO 24G
