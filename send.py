import pika


connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

channel = connection.channel()

channel.basic_publish(exchange = 'test-exchange', routing_key = 'hello',body = 'Check This ')

print('[x] sent --> New Message')

connection.close()