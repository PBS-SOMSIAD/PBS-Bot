# Use official Python base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies (if needed for pip packages)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
 && rm -rf /var/lib/apt/lists/*

# Copy and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt python-dotenv

# Copy application code
COPY . .

# Set environment variables for Python
ENV PYTHONUNBUFFERED=1

# Default command to run the app
CMD ["python", "main.py"]
