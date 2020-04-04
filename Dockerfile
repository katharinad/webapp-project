FROM python:3.6-slim
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install --user -r requirements.txt
COPY . /app
EXPOSE 5000
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app-hello-world:app"]
