#!/bin/bash
python3.9 -m venv build_venv
source build_venv/bin/activate
pip install -r requirements.txt
python manage.py collectstatic --noinput
python manage.py migrate --noinput
