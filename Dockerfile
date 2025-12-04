FROM runpod/worker:py3.10-cuda12.1

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python3", "worker.py"]
