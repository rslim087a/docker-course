FROM python:3.8-slim

WORKDIR /usr/service/grade-submission-application

COPY grade-submission/ .

RUN pip install -r grade-submission/requirements.txt

EXPOSE 8080

CMD ["python", "grade-submission/app.py"]