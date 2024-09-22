# Use the official Python 3.11 slim image from the Docker Hub
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file into the container at /app
COPY deployment_requirements.txt .

# Install all dependencies from requirements.txt
RUN pip3 install -Ur deployment_requirements.txt 

# Install PyTorch and related packages
RUN pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu

# Copy the src folder into the container at /app/src
COPY src ./src

# Copy the model folder into the container at /app/models
COPY models ./models

# Copy the gradio_app.py file into the container at /app
COPY gradio_app.py .

EXPOSE 7860
ENV GRADIO_SERVER_NAME="0.0.0.0"

# Run the Gradio app
CMD ["python3", "gradio_app.py"]