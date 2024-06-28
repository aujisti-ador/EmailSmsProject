# # Dockerfile
# FROM python:3.9-slim

# # Set environment variables
# ENV PYTHONDONTWRITEBYTECODE=1
# ENV PYTHONUNBUFFERED=1

# # Install MySQL client and development libraries
# # Install system dependencies
# RUN apt-get update \
#     && apt-get install -y gcc \
#     && apt-get install -y default-libmysqlclient-dev \
#     && apt-get install -y pkg-config \
#     && apt-get clean

# RUN mkdir /app
# WORKDIR /app

# # Copy requirements.txt from two directories up 
# COPY requirements.txt /app/
# RUN pip install --no-cache-dir -r requirements.txt


# # Install cron
# RUN apt-get update && apt-get install -y cron

# # Copy the rest of the application code
# COPY . /app/

# # Add crontab file in the cron directory
# RUN echo "* * * * * /usr/local/bin/python /usr/src/app/manage.py crontab run 609ec7706cc7c086d0f86303f734e699 >> /var/log/cron.log 2>&1" > /etc/cron.d/simple-cron

# # Give execution rights on the cron job
# RUN chmod 0644 /etc/cron.d/simple-cron

# # Apply cron job
# RUN crontab /etc/cron.d/simple-cron

# # Create the log file to be able to run tail
# RUN touch /var/log/cron.log

# # Run the command on container startup
# CMD cron && tail -f /var/log/cron.log


# Dockerfile

FROM python:3.9-slim

# Set the working directory
WORKDIR /usr/src/app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    default-libmysqlclient-dev \
    libssl-dev \
    cron

# Install Python dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Create the static and staticfiles directories
RUN mkdir -p /usr/src/app/static /usr/src/app/staticfiles

# Install cron
RUN apt-get update && apt-get install -y cron

# Create the log file to be able to run tail
RUN touch /var/log/cron.log

# Make the entrypoint script executable
COPY entrypoint.sh /usr/src/app/entrypoint.sh
RUN chmod +x /usr/src/app/entrypoint.sh

# Expose port for Django
EXPOSE 8000

# Command to run on container startup
CMD ["/usr/src/app/entrypoint.sh"]
