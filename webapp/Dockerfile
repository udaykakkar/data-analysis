FROM python:latest

RUN apt-get update && apt-get install -y wget

WORKDIR /data-analysis/webapp

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 9001

CMD [ "python", "./app.py" ]
