# Use the official Python image from the Docker Hub
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY api_requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r api_requirements.txt

RUN pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu

# Copy the source code into the container
COPY src ./src

# Copy the models into the container
COPY models ./models

# Copy the application code into the container
COPY app.py .

# Expose the port the app runs on
EXPOSE 8000

# Command to run the application
CMD ["python3", "app.py"]

# docker run -d -p 8000:8000 fastapi-app