import zmq
import time
import os

def start_pubsub():
	pub_port = os.environ['PUB_PORT']
	sub_port = os.environ['SUB_PORT']    
	context = zmq.Context()

	# create subscriber socket on port 60053
	frontend = context.socket(zmq.PULL)
	frontend.bind("tcp://*:" + pub_port)
	
	# create publisher socket on port 60054
	backend = context.socket(zmq.PUB)
	backend.bind("tcp://*:" + sub_port)

	# connect frontend and backend using proxy.
	zmq.proxy(frontend, backend)
    
	# We never get here...
	frontend.close()
	backend.close()
	context.term()
