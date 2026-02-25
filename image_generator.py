from diffusers import StableDiffusionPipeline
import torch
import os

pipe = StableDiffusionPipeline.from_pretrained(
    "runwayml/stable-diffusion-v1-5",
    torch_dtype=torch.float16
).to("cuda")

def generate_image(prompt, page_number):
    image = pipe(prompt).images[0]

    if not os.path.exists("images"):
        os.makedirs("images")

    path = f"images/page_{page_number}.png"
    image.save(path)
    return path
