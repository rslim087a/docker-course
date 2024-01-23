# Use an official Python runtime as a base image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /usr/src/

# Copy the project files into the working directory
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install -r flask-postgresql/requirements.txt

# Document that the application will be using port 3000.
EXPOSE 3000

# Run app.py when the container launches
CMD ["python", "flask-postgresql/app.py"]
