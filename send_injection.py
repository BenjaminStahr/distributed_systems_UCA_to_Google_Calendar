import pika
import json
connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
channel = connection.channel()


channel.queue_declare(queue='MessageQueue')

channel.basic_publish(exchange='',
                      routing_key='MessageQueue',
                      body=json.dumps({
            "summary": "tarea para SD!!!",
            "description": "A chance to hear more about Googles developer products.",
            "start": {
                "dateTime": "2019-04-28T13:00:00+02:00",
                "timeZone": "Europe/Madrid"
            },
            "end": {
                "dateTime": "2019-04-28T14:00:00+02:00",
                "timeZone": "Europe/Madrid"
            },
            "attendees": [
                {"email": "johntitorium@gmail.com"}
            ]
        }))

print(" [x] Sent 'Hello Worldd!'")
connection.close()
