from llama_cpp import Llama

llm = Llama(
      model_path="llama_cpp/llama.cpp/models/DeepSeek-R1-Distill-Qwen-32B-Q4_K_M.gguf",
      n_gpu_layers=10, # Uncomment to use GPU acceleration
      # seed=1337, # Uncomment to set a specific seed
      # n_ctx=2048, # Uncomment to increase the context window
      #cache-type-k="q8_0"
)

query = "I am unable to run CheckM on Galaxy. Previously, I used the public server galaxy.org, but it showed the message," \
    " “The job was terminated because it was using more memory than allocated.”" \
    " I attempted to run the same job with smaller files in the MB range, but the problem persisted." \
    " I then tried using other Galaxy servers, and now I am receiving an error stating, “Problem with the dataset.” However," \
    " the dataset contains only FASTA files. Can someone please help me with this issue?"

output = llm(
      "<｜User｜>" + query + "<｜Assistant｜>", # Prompt
      max_tokens=1000, # Generate up to 32 tokens, set to None to generate up to the end of the context window
      #stop=["Q:", "\n"], # Stop generating just before the model would generate a new question
      #echo=True # Echo the prompt back in the output
) # Generate a completion, can also call create_completion
print(output["choices"][0]["text"])