
import pika,sys,os

class ReceiveData(object):
    def __init__(self):
        self._connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        self._channel = self._connection.channel()

    
    def callback(self,ch,method,properties,body):
        print('[x] Received %r' %body)

    def consume(self,queue ='hello'):
        self._channel.basic_consume(queue='hello',auto_ack = True,on_message_callback = self.callback)
        print(' [*] Waiting for messages. To exit press CTRL+C')
        self._channel.start_consuming()



if __name__=="__main__":
    server = ReceiveData()
    server.consume(queue = 'hello')

# connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

# channel = connection.channel()
# channel.basic_consume(queue = 'hello',auto_ack=True,on_message_callback = callback)


# print(' [*] Waiting for messages. To exit press CTRL+C')
# channel.start_consuming()

# if __name__ == '__main__':
#     try:
#         main()
#     except KeyboardInterrupt:
#         print('Interrupted')
#         try:
#             sys.exit(0)
#         except SystemExit:
#             os._exit(0)
