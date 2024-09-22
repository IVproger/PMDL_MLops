# Use the official Python 3.11 slim image from the Docker Hub
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY deployment_requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r deployment_requirements.txt

# Copy the src folder into the container at /app/src
COPY src ./src

# Copy the model folder into the container at /app/model
COPY models ./models

# Copy the gradio_app.py file into the container at /app
COPY gradio_app.py .

# Specify the command to run your Gradio application
CMD ["python", "gradio_app.py"]