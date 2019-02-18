import threading
import msgqueue
import pubsub

def main():
        tasks = [msgqueue.start_msgqueue, pubsub.start_pubsub]
        for task in tasks:
                t = threading.Thread(target=task)
                t.start()

if __name__ == "__main__":
	main()
