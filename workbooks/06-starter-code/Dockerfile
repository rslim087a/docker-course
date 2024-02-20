FROM python:3.8-slim

WORKDIR /src/app/

COPY . .

RUN pip install -r global-superstore/requirements.txt

EXPOSE 8080

CMD ["python", "global-superstore/app.py"]