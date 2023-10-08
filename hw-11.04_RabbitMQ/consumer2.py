#!/usr/bin/env python
# coding=utf-8
import pika

credentials = pika.PlainCredentials('admin', 'kukushka')
parameters = pika.ConnectionParameters('192.168.1.108', '5672', '/', credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()
channel.queue_declare(queue='weather')


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body.decode())


channel.basic_consume(on_message_callback=callback, queue='weather', auto_ack=True)
channel.start_consuming()
