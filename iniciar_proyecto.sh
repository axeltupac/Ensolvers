#!/bin/bash


python3 -m venv virtual_env
source virtual_env/bin/activate
pip install -r requeriments.txt
python manage.py makemigrations
python manage.py migrate
python manage.py makemigrations items
python manage.py migrate items
python manage.py runserver

