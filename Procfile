release: python manage.py migrate
worker: celery -A getdiscount worker -B
web: gunicorn getdiscount.wsgi