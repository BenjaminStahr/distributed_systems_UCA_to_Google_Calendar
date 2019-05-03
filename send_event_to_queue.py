import pika
import json
def send_event(message):
    connection = pika.BlockingConnection(pika.ConnectionParameters(
            host='localhost'))
    channel = connection.channel()


    channel.queue_declare(queue='MessageQueue')

    channel.basic_publish(exchange='',
                          routing_key='MessageQueue',
                          body=json.dumps(message))

    print(" [x] %s was sent"% message['summary'])
    connection.close()
