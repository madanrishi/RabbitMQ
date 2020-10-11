import pika
import random

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

channel = connection.channel()
randomGen = str(random.randint(1,100000))
channel.basic_publish(exchange = '', routing_key = 'hello',body = randomGen)

print('[x] sent --> {}'.format(randomGen))

connection.close()