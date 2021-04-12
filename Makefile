runserver:
	poetry run python fakedata/manage.py runserver

makemigrations:
	poetry run python fakedata/manage.py makemigrations

migrate:
	poetry run python fakedata/manage.py migrate

collectstatic:
	poetry run python fakedata/manage.py collectstatic --no-input

createsuperuser:
	poetry run python fakedata/manage.py createsuperuser

shell:
	poetry run python fakedata/manage.py shell

lint:
	poetry run flake8
