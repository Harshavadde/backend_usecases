import threading
import time

class Queue:
    def __init__(self,k):
        self.queue = []
        self.size=0
        self.capacity=k
        self.lock = threading.Lock()

    def push(self,item):
        while True:
            with self.lock:
                if self.size < self.capacity:
                    self.queue.append(item)
                    self.size += 1
                    return
                print("Queue is full wait for release time:")
                break

    def pop(self,k):
        while True:
            with self.lock:
                if self.size >= k:
                    self.queue.pop(0)
                    self.size -= k
                    return
                print("Queue is empty wait for release time:")
                break

    def produce(self,item):
        for i in range(item):
            self.push(i)
            self.display()

    def consume(self,item):
        for i in range(item):
            self.pop(i)
            self.display()

    def display(self):
        print(self.queue)

obj = Queue(5)
t1=threading.Thread(target=obj.produce,args=(7,))
t2=threading.Thread(target=obj.consume,args=(1,))
t1.start()
t2.start()
t1.join()
t2.join()
