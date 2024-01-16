FROM python:3.8-slim

WORKDIR /usr/service/flask-mysql-application

COPY . .

RUN pip install -r flask-mysql/requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]
