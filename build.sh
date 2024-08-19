#!/usr/bin/env bash
# exit on error
set -o errexit

pip install --upgrade pi
python manage.py collectstatic --no-input
python manage.py migrate
