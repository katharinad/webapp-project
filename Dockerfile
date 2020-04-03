FROM python:3.6-slim
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
COPY . /app
EXPOSE 5000
CMD ["python", "./app-hello-world.py"]
