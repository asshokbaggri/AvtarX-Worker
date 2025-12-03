FROM runpod/worker:latest

# Install dependencies
COPY requirements.txt /requirements.txt
RUN pip install --upgrade pip
RUN pip install -r /requirements.txt

# Copy app files
COPY . /app
WORKDIR /app

CMD ["python3", "-u", "rp_handler.py"]
