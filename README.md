### How to install llama-cpp-python

- sudo apt install libgomp1 libomp-dev
- sudo apt install --reinstall gcc g++
- export CC=gcc
- export CXX=g++
- CMAKE_ARGS="-DLLAMA_OPENMP=ON -DCMAKE_C_COMPILER=gcc -DCMAKE_CXX_COMPILER=g++" pip install llama-cpp-python --no-cache-dir
- or CMAKE_ARGS="-DLLAMA_OPENMP=ON -DCMAKE_C_COMPILER=gcc -DCMAKE_CXX_COMPILER=g++" pip install llama-cpp-python --no-cache-dir --extra-index-url https://abetlen.github.io/llama-cpp-python/whl/cu121

### Run llama.cpp via Docker

https://github.com/unslothai/llama.cpp/blob/master/docs/docker.md

on CPUs

`docker run -v /home/ubuntu/data/ai_assistant/ai_assistant/models:/models ghcr.io/ggerganov/llama.cpp:light -m /models/DeepSeek-R1-Distill-Qwen-32B-Q4_K_M.gguf -p "Building a website can be done
 in 10 simple steps:" -n 512`

 on GPUs
