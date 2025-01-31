### How to install llama-cpp-python

- sudo apt install libgomp1 libomp-dev
- sudo apt install --reinstall gcc g++
- export CC=gcc
- export CXX=g++
- CMAKE_ARGS="-DLLAMA_OPENMP=ON -DCMAKE_C_COMPILER=gcc -DCMAKE_CXX_COMPILER=g++" pip install llama-cpp-python --no-cache-dir
- or CMAKE_ARGS="-DLLAMA_OPENMP=ON -DCMAKE_C_COMPILER=gcc -DCMAKE_CXX_COMPILER=g++" pip install llama-cpp-python --no-cache-dir --extra-index-url https://abetlen.github.io/llama-cpp-python/whl/cu121