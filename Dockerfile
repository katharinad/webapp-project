FROM python:3.6-slim as builder
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install --user -r requirements.txt
COPY . /app
EXPOSE 5000
CMD ["python", "./app.py"]

FROM nginx 
COPY --from=builder 