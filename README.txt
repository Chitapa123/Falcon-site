
Falcon Inch Intelligences - Django project skeleton
----------------------------------------
How to run locally:

1. Create a virtualenv and install Django (tested with Django 4.x)
   python -m venv venv
   source venv/bin/activate   (on Windows: venv\Scripts\activate)
   pip install django

2. From the folder containing manage.py, run:
   python manage.py runserver

3. Open http://127.0.0.1:8000/ in your browser.

Notes:
- This is a simple starter skeleton (DEBUG=True). Replace SECRET_KEY in settings.py for production.
- Static files are in falcon_project/main/static/main/
- Templates are in falcon_project/main/templates/main/
