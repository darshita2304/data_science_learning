from __future__ import absolute_import
from celery import Celery

app = Celery('tasksceduling_celery',
             broker='pyamqp://guest:guest@localhost:15672/',
             backend='rpc://',
             include=['tasksceduling_celery.tasks'])
