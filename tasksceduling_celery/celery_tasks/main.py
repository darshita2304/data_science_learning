from __future__ import absolute_import
from celery import Celery

app = Celery('celery_tasks',
             broker='pyamqp://guest:guest@localhost:15672/',
             backend='rpc://',
             include=['celery_tasks.tasks'])
