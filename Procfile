web: gunicorn fakedata.wsgi --log-file -
worker: celery worker --app=tasks.app
