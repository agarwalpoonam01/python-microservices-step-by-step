# syntax=docker/dockerfile:1
FROM python:3.8
WORKDIR /code
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
CMD ["python3", "app.py"]
EXPOSE 5000