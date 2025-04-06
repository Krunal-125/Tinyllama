from huggingface_hub import snapshot_download

# Download the model to a local folder
snapshot_download(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    local_dir="./Tinyllama",
    local_dir_use_symlinks=False
)