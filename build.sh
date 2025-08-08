#!/usr/bin/env bash

# Install Python dependencies
pip install -r requirements.txt

# Optional: run migrations
python manage.py migrate

# Optional: collect static files (if you're using them)
python manage.py collectstatic --noinput
