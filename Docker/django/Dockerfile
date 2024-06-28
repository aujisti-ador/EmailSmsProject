# # Dockerfile

FROM python:3.9-slim

# Set the working directory
WORKDIR /usr/src/app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    default-libmysqlclient-dev \
    libssl-dev \
    cron \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Create the static and staticfiles directories
RUN mkdir -p /usr/src/app/static /usr/src/app/staticfiles

# Create the log file to be able to run tail
RUN touch /var/log/cron.log

# Copy entrypoint script into the image
COPY entrypoint.sh /usr/src/app/entrypoint.sh
RUN chmod +x /usr/src/app/entrypoint.sh

# Run the command on container startup
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
