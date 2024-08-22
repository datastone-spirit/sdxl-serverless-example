import torch
from sprite_gpu import start, Env
from diffusers import DiffusionPipeline
from typing import Dict, Any
from PIL import Image

pipe = DiffusionPipeline.from_pretrained("/workspace/sdxl-base", force_download=False, torch_dtype=torch.float16, use_safetensors=True, variant="fp16")
pipe.to("cuda")


def to_base64(images: Image.Image):
    import io
    import base64

    im = images.convert("RGB")
    with io.BytesIO() as output:
        im.save(output, format="PNG")
        contents = output.getvalue()
        return base64.b64encode(contents).decode("utf-8")

def handler(request: Dict[str, Any], env: Env):
    output = f"hello world! {request}"
    input = request.get("input")
    prompt = input.get("prompt")
    images = pipe(prompt=prompt).images[0]
    result = '{"image": "%s"}' % to_base64(images)
    return result


start({"handler": handler })
