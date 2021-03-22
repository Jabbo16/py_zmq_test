import sys
import zmq

port = sys.argv[1]
ip = sys.argv[0]

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.setsockopt(zmq.SUBSCRIBE, "")

print "Message received..."
socket.bind("tcp://%s:%s" % (ip, port))

while True:
    print socket.recv()
