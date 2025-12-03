import requests
import torch
from PIL import Image
from io import BytesIO
from src.model import load_model
from src.utils import upload_to_r2

pipe = None

def init_model():
    global pipe
    if pipe is None:
        pipe = load_model()
    return pipe

def generate_avatar_video(image_url, prompt, duration):
    model = init_model()

    img_bytes = requests.get(image_url).content
    input_img = Image.open(BytesIO(img_bytes)).convert("RGB")

    frames = []
    steps = duration * 8

    for i in range(steps):
        out = model(prompt=prompt, image=input_img, strength=0.6).images[0]
        frames.append(out)

    # Save as video
    save_path = "/tmp/avatar.mp4"
    frames[0].save(
        save_path,
        save_all=True,
        append_images=frames[1:],
        duration=40,
        loop=0
    )

    return upload_to_r2(save_path)
