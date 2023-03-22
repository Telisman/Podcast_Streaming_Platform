import pytest
from django.conf import settings
from django.db import connections

@pytest.fixture(scope='session')
def django_db_setup():
    settings.DATABASES['default'] = {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'streming_db',
        'USER': 'root',
        'PASSWORD': 'Opke1987.',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }

@pytest.fixture
def db():
    connection = connections['default']
    yield connection
    connection.close()