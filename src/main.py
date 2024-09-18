import torch
from spirit_gpu import start, Env
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

def get_valid_value(data: Dict, key: str, default_value: str, is_valid) -> int :
   value = int(data.get(key, default_value)) 

   if is_valid(value):
       return value
   return int(default_value)

def handler(request: Dict[str, Any], env: Env):
    print(f"hello world! {request}")
    input = request.get("input")
    height = get_valid_value(request, "height", "768", lambda x: x > 512 and x <= 1024)
    width = get_valid_value(request, "width", "768", lambda x: x > 512 and x <= 1024)
    num_inference_steps = get_valid_value(request, "num_inference_steps", "20", lambda x: x >= 4 and x <= 50)

    prompt = input.get("prompt")
    images = pipe(prompt=prompt,
                  height = height,
                  width = width,
                  num_inference_steps=num_inference_steps).images[0]
    base64_image = to_base64(images)
    print(f"result len is {len(base64_image)}")
    result = '{"image": "%s"}' % base64_image
    return result


start({"handler": handler })
