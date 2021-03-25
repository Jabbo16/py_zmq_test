import zmq
import random
import time
import sys

port = sys.argv[1]
ip = sys.argv[0]

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://172.21.0.1:8000")
socket.connect("tcp://172.21.0.1:8000")
socket.connect("tcp://%s:%s" % (ip, port))

topic = 0

while True:
    topic = topic + 1
    messagedata = topic
    print "Message sent: %d %d" % (topic, messagedata)
    socket.send("%d %d" % (topic, messagedata))
    time.sleep(1)
