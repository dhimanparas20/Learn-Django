# Use an official Python runtime as a parent image
FROM python:3.10-slim

# # Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app/

# # Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 5000 to the outside world
EXPOSE 5000

# Run Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "your_project_name.wsgi:application"]
# Run uvicorn for longlived connections (eg. Websockets)
# CMD ["uvicorn", "your_project_name.asgi:application", "--host", "0.0.0.0", "--port", "8000"]