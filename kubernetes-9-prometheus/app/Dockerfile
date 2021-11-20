FROM python:3.9-slim-buster
RUN apt-get update -qq
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 8000
ENV FLASK_APP=app.py
ENV FLASK_ENV=development
COPY . .
CMD  ["flask", "run", "--port=8000",  "--host=0.0.0.0"]