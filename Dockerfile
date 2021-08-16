FROM python:latest

RUN pip install -r requirements.txt

#ENTRYPOINT [ "uvicorn"]

#CMD ["uvicorn","main:app","--reload"]