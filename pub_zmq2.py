import zmq
import random
import time
import sys

port = sys.argv[2]
ip = sys.argv[1]

address = "tcp://{}:{}".format(ip, port)

context = zmq.Context()
socket = context.socket(zmq.PUB)
print(address)
socket.connect(address)

topic = 0

while True:
    topic = topic + 1
    messagedata = topic
    print("Message sent: %d %d" % (topic, messagedata))
    socket.send_string("%d %d" % (topic, messagedata))
    time.sleep(1)
