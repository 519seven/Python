"""Sample script to attach to zmq endpoint on the PX"""

import time
import zmq

print "Attaching to zmq socket..."

addr = 'ipc:///var/run/z.zmq'
ctx = zmq.Context()
s2 = ctx.socket(zmq.SUB)
s2.setsockopt(zmq.SUBSCRIBE, '')
s2.connect(addr)

# Sleep to allow sockets to connect.
time.sleep(1.0)

while True:
    print s2.recv()
