from diffusers import DiffusionPipeline
import torch

def load_model():
    pipe = DiffusionPipeline.from_pretrained(
        "SG161222/Realistic_Vision_V5.1",
        torch_dtype=torch.float16
    ).to("cuda")

    return pipe
