from fakedata.celery import app

from schemas.service import generate_csv
from schemas import models


@app.task
def start_generator(pk):
    dataset = models.Dataset.objects.get(id=pk)
    generate_csv(dataset)
