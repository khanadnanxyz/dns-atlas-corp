#!/bin/sh
source venv/bin/activate
exec gunicorn --chdir web main:app -w 1 --threads 2 -b 0.0.0.0:5000
