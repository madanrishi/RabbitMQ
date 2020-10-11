import pika
import random

class RabbitMq(object):
    def __init__(self,queue = 'test-queue'):
        self._connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        self._channel = self._connection.channel()
        self.queue = queue
        self._channel.queue_declare(queue = self.queue)

    def publish(self,payload = {}):
        self._channel.basic_publish(exchange = '',
                                    routing_key = 'hello',
                                    body = str(payload))
        self._connection.close()


if __name__ =="__main__":
    server = RabbitMq(queue='hello')
    randomGen = str(random.randint(1,100000))
    server.publish(payload = {"data":randomGen})
