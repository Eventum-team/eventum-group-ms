FROM python:3.6

EXPOSE 5000

WORKDIR /eventum-group-ms

COPY . .

ENV FLASK_APP=resources

RUN pip install -e .

CMD flask run --host=0.0.0.0