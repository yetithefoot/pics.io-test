FROM python:3.8-alpine3.14

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

VOLUME [ "/var/log/nginx/" ]

EXPOSE 5000

CMD ["python3", "app.py"]

