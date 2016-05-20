#!/usr/bin/env python
from flask import Flask
import pika

QUEUE_NAME = 'baby-queue'
RMQ_HOST = 'rabbitmq'

app = Flask(__name__)


def send_message(message):
    connection = pika.BlockingConnection(pika.ConnectionParameters(RMQ_HOST))
    channel = connection.channel()
    channel.queue_declare(queue=QUEUE_NAME)
    channel.basic_publish(exchange='', routing_key=QUEUE_NAME, body=message)
    connection.close()

@app.route('/')
def index():
    message = 'Visitor came to your website.'
    send_message(message)
    return 'Sent a message to rabbitmq: {}'.format(message)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
