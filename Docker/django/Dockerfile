# Dockerfile
FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install MySQL client and development libraries
RUN apt-get update && apt-get install -y \
    default-libmysqlclient-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir /app
WORKDIR /app

# Copy requirements.txt from two directories up
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . /app/

# Uncomment the lines below if you want to use a non-root user
# RUN useradd appuser
# USER appuser
