import requests
import os

R2_URL = os.getenv("CLOUDFLARE_R2_URL")
R2_KEY = os.getenv("CLOUDFLARE_R2_KEY")
R2_SECRET = os.getenv("CLOUDFLARE_R2_SECRET")

def upload_to_r2(file_path):
    with open(file_path, "rb") as f:
        data = f.read()

    res = requests.put(
        R2_URL,
        data=data,
        headers={
            "X-Auth-Key": R2_KEY,
            "X-Auth-Email": "your_email",
            "Content-Type": "video/mp4"
        }
    )

    if res.status_code in [200, 204]:
        return R2_URL
    else:
        raise Exception("Upload failed: " + res.text)
