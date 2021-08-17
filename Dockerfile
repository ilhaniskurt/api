# Python Image
FROM python:latest

WORKDIR /app

# Install Dependencies 
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .