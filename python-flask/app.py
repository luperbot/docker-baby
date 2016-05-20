#!/usr/bin/env python
import datetime

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
    now = datetime.datetime.now()
    message = 'Visitor came to your website @ {}.'.format(now)
    send_message(message)
    return 'Sent a message to rabbitmq: {}'.format(message)

def get_messages():
    messages = []
    connection = pika.BlockingConnection(pika.ConnectionParameters(RMQ_HOST))
    channel = connection.channel()
    while True:
        method_frame, header_frame, body = channel.basic_get(QUEUE_NAME)
        if not method_frame:
            connection.close()
            return messages
        messages.append(body)
        channel.basic_ack(method_frame.delivery_tag)

@app.route('/inbox')
def inbox():
    messages = get_messages()
    return 'You have the following messages: {}'.format(messages)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
