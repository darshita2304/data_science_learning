#!/usr/bin/env python
import pika
import sys
import os
import time


def main():
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='hello')

    # def callback(ch, method, properties, body):
    #     print(f" [x] Received {body}")

    def hello_queue_callback(ch, method, properties, body):
        print("Hello Queue Handler....")
        print(f" [x] Received {body.decode()}")
        time.sleep(body.count(b'.'))
        print(" [x] Done")
        ch.basic_ack(delivery_tag=method.delivery_tag)

    def test_queue_callback(ch, method, properties, body):
        print("Test Queue Handler....")
        print(f" [x] Received {body.decode()}")
        time.sleep(body.count(b'.'))
        print(" [x] Done")
        ch.basic_ack(delivery_tag=method.delivery_tag)

    # don't dispatch a new message to a worker until it has processed and acknowledged the previous one.
    # Instead, it will dispatch it to the next worker that is not still busy. one at a time
    channel.basic_qos(prefetch_count=1)

    channel.basic_consume(
        queue='hello', on_message_callback=hello_queue_callback, auto_ack=True)

    channel.basic_consume(
        queue='test', on_message_callback=test_queue_callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
