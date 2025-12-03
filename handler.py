import runpod
from src.inference import generate_avatar_video

def handler(job):
    try:
        img_url = job["input"].get("image_url")
        prompt  = job["input"].get("prompt", "handsome cinematic avatar")
        duration = job["input"].get("duration", 5)

        output_url = generate_avatar_video(img_url, prompt, duration)

        return {
            "status": "success",
            "video_url": output_url
        }

    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }

runpod.serverless.start({"handler": handler})
