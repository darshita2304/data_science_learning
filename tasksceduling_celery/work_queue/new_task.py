import pika
import sys


connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')

# make sure that the queue will survive a RabbitMQ node restart. In order to do so, we need to declare it as durable:
channel.queue_declare(queue='task_queue', durable=True)

message = ' '.join(sys.argv[1:]) or "Hello World!"

# At that point we're sure that the task_queue queue won't be lost even if RabbitMQ restarts. Now we need to mark our messages as persistent - by supplying a delivery_mode property with the value of pika.DeliveryMode.Persistent
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body=message, properties=pika.BasicProperties(
                          delivery_mode=pika.DeliveryMode.Persistent)
                      )
print(f" [x] Sent {message}")


connection.close()
