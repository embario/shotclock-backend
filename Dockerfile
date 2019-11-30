from python:3.7

RUN apt-get update

WORKDIR /build
COPY requirements.txt /build
RUN pip install -r requirements.txt

ADD . /app
WORKDIR /app

EXPOSE 8000

ENTRYPOINT ["python", "manage.py", "runserver", "0.0.0.0:8000"]