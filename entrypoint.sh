#!/bin/bash

# Apply database migrations
python manage.py migrate

service cron restart

# Collect static files
python manage.py collectstatic --noinput

# Remove existing crontabs and add new ones
python manage.py crontab remove
python manage.py crontab add

# Start cron service in the background
service cron start

# Tail the cron log to keep the container running
tail -f /var/log/cron.log &

# Start Django server with gunicorn
exec gunicorn backend.wsgi:application --bind 0.0.0.0:8000
