FROM ghcr.io/gotoeveryone/python-with-pipenv:3.9.6

ENV TZ Asia/Tokyo

RUN apt-get update \
  && apt-get -y install libpq-dev gcc \
  && pip install psycopg2
