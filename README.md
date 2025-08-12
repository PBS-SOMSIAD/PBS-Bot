# P.A.T.R.Y.K

###
all dependencies are in requirements.txt

# Installation

```bash
pip install -r requirements.txt
```
or if you have installed uv

# Usage

```bash
python main.py
```

## Configuration
You need to fill in the '.env' file with your own values.

# Environment Variables
- `MODEL`: The model to use, e.g., `qwen3:1.7b`.
- `BASE_URL`: The base URL for the model server, e.g., `http://localhost:11434/v1`.

if you haven't installed modle locally, you can use the following command to download it:
```bash
ollama pull qwen3:1.7b
```
