FROM python:latest

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

#ENTRYPOINT [ "uvicorn"]

#CMD ["uvicorn","main:app","--reload"]