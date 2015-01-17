
FROM orchardup/python:2.7
ADD . /code
WORKDIR /code
RUN apt-get update
RUN apt-get install libpq-dev -y
RUN pip install -r requirements.txt
