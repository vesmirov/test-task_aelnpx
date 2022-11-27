# FakeCSV
![CI](https://github.com/vilagov/fake-csv/workflows/FakeCSV%20CI/badge.svg)

## Description:
FakeCSV is an online service for generating CSV files with fake(dummy) data.

The service allows you to generate large amounts of data, which you can use to test your projects.
Csv generation process takes from a second to several minutes, depending on the specified parameters and the required amount of data. It's fully background process, so you can check status anytime and download the file later, when it's ready.

## Deployment:

### Heroku

FakeCSV is configured for deployment on Heroku.
So before deployment you need to be sure, that you have an [account](https://heroku.com) on the platform.

More detail instructions for setting up heroku and apps you can find in [official Heroku guide](https://devcenter.heroku.com/articles/getting-started-with-python).

#### Steps:

1. `git clone` project to local repository.

2. [Install](https://devcenter.heroku.com/articles/getting-started-with-python#set-up) Heroku CLI.

3. Login via `heroku login`.

4. Being at the save level with manage.py, create your Heroku app - `heroku create your-app-name`.

5. The project uses Celery library with Redis BSD. So you need to add redis addon to your dyno before pushing code to Heroku:

   5.1. [provide](https://dashboard.heroku.com/account/billing) your card information. Don't be afraid, there is no charges if you using hobby-dev plan;

   5.2. add addon to your Heroku app - `heroku addons:create heroku-redis:hobby-dev`;

   5.3. wait until redis addon is ready;

   5.4 add to your Heroku app configuration next variables: `SECRET_KEY` (your django secret key) and `HOST` (your Heroku app url).  
   You can add them through `heroku config:set SECRET_KEY=<your_django_secret_key> HOST=<your_app_url>`  
   If you need django with debug mode, you can also add `DEBUG=True` variable.

5. Push local project to your Heroku app - `git push heroku main`.

6. Create superuser for project - `heroku run python manage.py createsuperuser`.

Now you can open website by typing `heroku open`.

## System requirements

* Ubuntu 16.^
* macOS High Sierra 10.13.6

## Improvement plans

* write unittests
* pack project to docker-compose
* add multiprocessing
* expand columns types list

## Stack

* [Python 3.9](https://www.python.org/)
* [Django 3](https://www.djangoproject.com/)
* [Celery 5](https://docs.celeryproject.org/)
* [Bootstrap 5](https://getbootstrap.com/)
* [Faker](https://faker.readthedocs.io/)

## Author

Evan Vesmirov

Linkedin: https://www.linkedin.com/in/vesmirov/

Email: evan.vesmirov@proton.me
