#!/usr/bin/env python
# coding=utf-8
import pika

credentials = pika.PlainCredentials('admin', 'kukushka')
parameters = pika.ConnectionParameters('192.168.1.108', 5672, '/', credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()
channel.queue_declare(queue='weather')
channel.basic_publish(exchange='', routing_key='weather', body='rain, wind')
connection.close()
