from celery import Celery

app = Celery('final',
             broker='amqp://darshita:darshita@localhost/',
             backend='rpc://')

app.conf.update(
    result_expires=3600,
)

# Ensure Celery autodiscovers tasks in the 'tasks' module
app.autodiscover_tasks(['final'])

if __name__ == '__main__':
    app.start()
