import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()


channel.queue_declare(queue='hello-queue')
flag = True
while flag:
    msg = input("Message: ")
    if msg == "exit":
        flag = False
        break
    channel.basic_publish(exchange='',
                        routing_key='hello-queue',
                        body=msg)
    print(" [x] Message Sent!")

connection.close()

