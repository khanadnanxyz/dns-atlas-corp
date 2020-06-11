#!/bin/sh
source venv/bin/activate
exec gunicorn -b :5000 --workers=1 --access-logfile - --error-logfile - app:app
