FROM nvidia/cuda:12.1.1-base-ubuntu22.04

WORKDIR /app

# Install Python + system deps
RUN apt-get update && \
    apt-get install -y python3 python3-pip git && \
    apt-get clean

COPY . /app

RUN pip3 install --no-cache-dir -r requirements.txt

CMD ["python3", "rp_handler.py"]
