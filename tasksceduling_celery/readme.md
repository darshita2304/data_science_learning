
## run in the parent folder of our project folder test_celery to run worker - middle layer for queue

celery -A tasksceduling_celery worker --loglevel=info

## In another console, input the following (run in the parent folder of our project folder test_celery):

python -m test_celery.run_tasks