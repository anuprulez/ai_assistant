./llama.cpp/build/bin/llama-cli \
       --model models/DeepSeek-R1-Distill-Qwen-32B-Q8_0.gguf \
       --cache-type-k q8_0 \
       --threads 16 \
       --prompt '<｜User｜>What is 1+1?<｜Assistant｜>' \
       --n-gpu-layers 50
       -no-cnv