#!/bin/bash

echo "activate the virtualenv"
source /workspace/ComfyUI/venv/bin/activate

# Before we start comfyui, we should copy extra_model_paths.yml from the storage (mounted with /root, we
# assume that the file was located at /root/comfyui_workspace/extra_model_paths.yml).

echo "copy extra models configuration"
cp /root/comfyui_workspace/extra_model_paths.yml /workspace/ComfyUI/extra_model_paths.yaml

echo "start comfyui in background....."
/workspace/ComfyUI/venv/bin/python /workspace/ComfyUI/main.py --listen=0.0.0.0 &

echo "pip list:"
/workspace/ComfyUI/venv/bin/python -m pip list 

echo "start serverless entrypoint: /workspace/ComfyUI/venv/bin/python -u /root/comfyui_workspace/main.py"
# we start the main programming, which was serverless entrypoints
/workspace/ComfyUI/venv/bin/python -u /root/comfyui_workspace/main.py
