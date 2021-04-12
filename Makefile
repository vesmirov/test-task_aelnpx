runserver:
	poetry run python manage.py runserver

gunicorn:
	poetry run gunicorn fakedata.wsgi:application -b 0:8000

makemigrations:
	poetry run python manage.py makemigrations

migrate:
	poetry run python manage.py migrate

collectstatic:
	poetry run python manage.py collectstatic --no-input

createsuperuser:
	poetry run python manage.py createsuperuser

shell:
	poetry run python manage.py shell

lint:
	poetry run flake8
