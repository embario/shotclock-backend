from python:3.7

RUN apt-get update

# Install postgresql-client for pg_dump
RUN apt-get install -y postgresql-client

WORKDIR /build
COPY requirements.txt /build
RUN pip install -r requirements.txt

ADD . /app
WORKDIR /app

EXPOSE 8000

CMD ["/bin/bash", "./run.sh"]