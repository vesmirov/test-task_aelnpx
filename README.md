# FakeCSV
![CI](https://github.com/vilagov/fake-csv/workflows/FakeCSV%20CI/badge.svg)

## Description:
FakeCSV is an online service for generating CSV files with fake(dummy) data.

The service allows you to generate large amounts of data that you can use to test your projects.
The generation process takes from a second to several minutes, depending on the specified parameters and the required amount of data.

## Deployment:

### Heroku

The project is configured for deployment on the Heroku.
So before deployment you need to be sure, that you have an account on [Platform](https://heroku.com).

Detailed instructions for setting up heroku you can find in [official Heroku guide](https://devcenter.heroku.com/articles/getting-started-with-python).

1. `git clone` project to local repository.

2. [Install](https://devcenter.heroku.com/articles/getting-started-with-python#set-up) Heroku CLI.

3. Login using `heroku login`.

4. Being in the save level with manage.py, create your heroku app through `heroku create your-app-name`.

5. The project using Celery library with Redis BSD. So you need to add redis addon to your dyno before pushing the code to heroku:
  1. [provide](https://dashboard.heroku.com/account/billing) your card information. Don't be afraid, there is no charges, if you using hobby-dev plan;
  2. add addon to your heroku app with command `heroku addons:create heroku-redis:hobby-dev`;
  3. wait until redis addon is ready;
  4. add to your heroku configuration next variables:
    * SECRET_KEY (your django secret key);
    * HOST (your heroku application url).
    You can add them through `heroku config:set SECRET_KEY=<your_django_secret_key> HOST=<your_app_url>`
    If you need to turn on django debug mode, you can also add `DEBUG=True` variable.

5. Push local project to your heroku app `git push heroku main`.

6. Create superuser `heroku run python manage.py createsuperuser`.

Now you can open website by typing `heroku open`.

## System requirements

* Ubuntu 16.^
* macOS High Sierra 10.13.6

## Improvement plans

* write unittests
* pack project to docker-compose
* add multiprocessing in project
* expand columns types list

## Stack

* [Python 3.9](https://www.python.org/)
* [Django 3](https://www.djangoproject.com/)
* [Celery 5](https://docs.celeryproject.org/)
* [Bootstrap 5](https://getbootstrap.com/)
* [Faker](https://faker.readthedocs.io/)

## Author

Evan Vilagov

Linkedin: https://www.linkedin.com/in/vilagov/
Email: evan.vilagov@gmail.com
