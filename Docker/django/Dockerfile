# Dockerfile
FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install MySQL client and development libraries
# Install system dependencies
RUN apt-get update \
    && apt-get install -y gcc \
    && apt-get install -y default-libmysqlclient-dev \
    && apt-get install -y pkg-config \
    && apt-get clean

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
