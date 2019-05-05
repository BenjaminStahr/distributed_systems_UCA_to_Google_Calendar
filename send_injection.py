import pika
import json
connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
channel = connection.channel()


channel.queue_declare(queue='MessageQueue')

channel.basic_publish(exchange='',
                      routing_key='MessageQueue',
                      body=json.dumps({
            "summary": "Notiz für morgen",
            "description": "sdfhsdfg.",
            "start": {
                "dateTime": "2019-05-03T14:00:00+02:00",
                "timeZone": "Europe/Madrid"
            },
            "end": {
                "dateTime": "2019-05-03T14:00:00+02:00",
                "timeZone": "Europe/Madrid"
            },
            "attendees": [
                {"email": "johntitorium@gmail.com"}
            ]
        }))

connection.close()
