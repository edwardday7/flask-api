FROM python:3.6-slim

ADD /app /app

WORKDIR /

RUN pip3 install flask gunicorn pyjwt googlemaps

CMD exec gunicorn -b :$PORT -w 1 app:app