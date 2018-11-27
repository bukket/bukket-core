FROM python:3.7-stretch

RUN apt-get update -y && apt-get install -y python-psycopg2

WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 3000

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:3000", "run:app"]


