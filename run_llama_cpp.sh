./llama.cpp/build/bin/llama-cli \
       --model models/DeepSeek-R1-Distill-Qwen-32B-Q4_K_M.gguf \
       --cache-type-k q8_0 \
       --threads 16 \
       --prompt '<｜User｜>What is 1+1?<｜Assistant｜>' \
       --threads 16 \
       ##--n-gpu-layers 40
       -no-cnv

# I have a dataset in which we are looking at canonical events vs noncanonical events (intro retention, alternative splicing, etc.). We were considering using STAR in a way were we can obtain counts only for canonical events and noncanonical events, to compare the quantifications afterwards. Do you think it is possible to use solely STAR to get these quantifications? If so, which would be the arguments one should change?
# https://github.com/alexdobin/STAR/issues/2259