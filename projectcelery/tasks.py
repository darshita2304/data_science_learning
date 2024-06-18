from celery import Celery
import celeryconfig

app = Celery()
app.config_from_object(celeryconfig)
#: Set default configuration module name
# os.environ.setdefault('CELERY_CONFIG_MODULE', 'celeryconfig')


@app.task
def add(x, y):
    return x + y


if __name__ == '__main__':
    args = ['worker', '--loglevel=INFO']
    app.worker_main(argv=args)
