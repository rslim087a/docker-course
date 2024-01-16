FROM python:3.8-slim

WORKDIR /usr/service/flask-mysql-application

COPY . .

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "grade-submission/app.py"]
