# Use an official Python runtime as a base image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /usr/service/flask-mysql-application

# Copy the requirements.txt file from the 'flask-mysql' folder into the container at /usr/service/flask-mysql-application
COPY flask-mysql/requirements.txt ./

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Copy the rest of the application's source code from the 'flask-mysql' folder
COPY flask-mysql/ .

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Run app.py when the container launches
CMD ["python", "app.py"]