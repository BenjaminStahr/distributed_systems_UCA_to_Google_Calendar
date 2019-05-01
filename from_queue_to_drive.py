import pika
import Drive_Authorization
import ast


connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
channel = connection.channel()


channel.queue_declare(queue='MessageQueue')


def callback(ch, method, properties, body):
    print(body.decode("utf-8"))
    Drive_Authorization.upload_file_to_drive(body.decode("utf-8"))


channel.basic_consume(queue='hello',
                      auto_ack=True,
                      on_message_callback=callback)


print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()