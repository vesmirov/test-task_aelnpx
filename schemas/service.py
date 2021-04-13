import os
import csv
import tempfile

from django.conf import settings
from django.core.files import File
import faker

CSV_PATH = os.path.join(settings.MEDIA_ROOT, 'csv')
FAKE = faker.Faker()
FAKES = {
    'FNAME': lambda conf: FAKE.name(),
    'JOB': lambda conf: FAKE.job(),
    'EMAIL': lambda conf: FAKE.email(),
    'DOMAIN': lambda conf: FAKE.domain_name(),
    'PHONE': lambda conf: FAKE.phone_number(),
    'COMPANY': lambda conf: FAKE.company(),
    'TEXT': lambda conf: ' '.join(FAKE.sentences(nb=conf['sentences'])),
    'INTEGER': lambda conf: FAKE.random_int(min=conf['min'], max=conf['max']),
    'ADDRESS': lambda conf: FAKE.address(),
    'DATE': lambda conf: FAKE.date(),
}


def get_data(dataset):
    """Service function, gets all necessary data from query"""

    data = {
        'name': f'{dataset.created.strftime("%m-%d-%Y-%H-%M-%S")}-'
                f'{dataset.id}',
        'string_character': dataset.schema.separator,
        'separator': dataset.schema.separator,
        'rows': dataset.rows,
        'columns': dataset.schema.columns.all(),
    }
    return data


def get_fake_row(columns):
    """Service function for generating fake row"""

    fake_row = []
    for col in columns:
        col_params = {
            'min': col.integer_from,
            'max': col.integer_to,
            'sentences': col.text_len,
        }
        fake_row.append(FAKES[col.column_type](col_params))
    return fake_row


def generate_csv(dataset):
    """
    Generates csv file in temporary directory,
    then saves it as File() in Dataset's object FileField
    """

    data = get_data(dataset)

    csv.register_dialect(
        'custom_dialect',
        delimiter=data['separator'],
        escapechar=data['string_character']
    )

    with tempfile.TemporaryFile(suffix='.csv', mode='w+') as file:
        writer = csv.writer(file, 'custom_dialect')

        titles = list(data['columns'].values_list('title', flat=True))
        writer.writerow(titles)

        for _ in range(data['rows']):
            fake_row = get_fake_row(data['columns'])
            writer.writerow(fake_row)

        dataset.status = dataset.Status.READY
        filename = CSV_PATH + '/' + data['name'] + '.csv'
        dataset.csv_file.save(filename, File(file))
