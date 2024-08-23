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
        print(f"len is {len(contents)}")
        return base64.b64encode(contents).decode("utf-8")

def handler(request: Dict[str, Any], env: Env):
    print(f"hello world! {request}")
    input = request.get("input")
    prompt = input.get("prompt")
    images = pipe(prompt=prompt,
                  height = 768,
                  width = 768,
                  num_inference_steps=20).images[0]
    result = '{"image": "%s"}' % to_base64(images)

    return result


start({"handler": handler })
