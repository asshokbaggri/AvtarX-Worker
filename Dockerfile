FROM runpod/worker:latest

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python3", "rp_handler.py"]
