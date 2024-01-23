# Use the official Maven runtime with JDK 17 as a base image
FROM maven:3.6.3-openjdk-17-slim

# Set the working directory in the container
WORKDIR /usr/src/

# Copy the project files
COPY global-superstore/ .

## 4. Document and inform the developer that the application will use the container port: 8080.
EXPOSE 8080

## 5. Define the command to run when the container starts.
CMD ["mvn", "clean", "spring-boot:run"]
