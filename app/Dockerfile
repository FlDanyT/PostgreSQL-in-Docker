FROM python:alpine

WORKDIR /app

RUN pip install psycopg2-binary

COPY . .

CMD [ "python", "main.py" ]