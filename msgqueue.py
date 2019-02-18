import zmq
import os

def start_msgqueue():
    router_port = os.environ['ROUTER_PORT']
    dealer_port = os.environ['DEALER_PORT']
    context = zmq.Context()    

    # create frontend socket at 60051
    frontend = context.socket(zmq.ROUTER)
    frontend.bind("tcp://*:" + router_port)
    
    # create backend socket at 60052
    backend  = context.socket(zmq.DEALER)
    backend.bind("tcp://*:" + dealer_port)

    # connect frontend and backend using proxy.
    zmq.proxy(frontend, backend)

    # We never get here...
    frontend.close()
    backend.close()
    context.term()
