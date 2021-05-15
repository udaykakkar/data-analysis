FROM python:latest

RUN pip3 install flask
RUN pip3 install requests
RUN pip3 install pandas

COPY . .

EXPOSE 9001

CMD ["python3", "app.py"]