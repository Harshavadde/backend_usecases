
import time
import threading
class Queue:
    def __init__(self,nf):
        self.queue = [0]*nf
        self.t=[7,6,5,4,3,2]
        self.pf = 0
        self.capacity = nf
        self.front = 0
        self.rear = 0
        self.size = 0
        self.lock = threading.Lock()

    def is_full(self):
        return self.size == self.capacity

    def is_empty(self):
        return self.size == 0

    def enqueue(self,val):
        if not self.is_full():
            self.queue[self.rear] = val
            print(f"Inserted {val} at index {self.rear}")
            self.rear = (self.rear + 1) % self.capacity
            self.size += 1

        else:
            if self.lock:
                x = self.pf
                delay = self.t[x % len(self.t)]
                print(f"Queue is full. it will overwrite index {x} with {val} after waiting {delay} seconds..." )
                time.sleep(delay)
                self.queue[x] = val
                self.pf = (self.pf + 1) % self.capacity
    def dequeue(self):
        if self.is_empty():
            print("Queue is empty, cannot dequeue")
            return None

        val = self.queue[self.front]
        self.queue[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return val
    def display(self):
        return self.queue

obj = Queue(5)
for i in range(5):
    obj.enqueue(i)

print("After first 5 enqueues:", obj.display())
for i in range(5, 10):
    obj.enqueue(i)
    print("Current queue:", obj.display())


# from datetime import datetime
# import time
# class Queue:
#     def __init__(self,k):
#         self.wt=[7,4,7,3,8]
#         self.t=[0]*k
#         self.pf=0
#         self.que= [0] * k
#         self.size=0
#         self.front=0
#         self.rear=0
#         self.cap=k
#     def enqueue(self,val):
#         if self.isfull():
#             time.sleep(5)
#             saved = self.t[0]
#             saved_time = datetime.now().replace(hour=saved[0], minute=saved[1], second=saved[2], microsecond=0)
#             current = datetime.now()
#             passed_seconds = (current - saved_time).total_seconds()
#             print(f"Execution time taken by {self.rear}:",passed_seconds)
#             wt = passed_seconds < self.wt[self.rear]
                  #if wt:
    #                 self.pf+=1
    #                 print("Resource is full")
#                 return
#             self.dequeue()
#             self.enqueue(val)
#             return
#         self.que[self.rear]=val
#         now=datetime.now()
#         self.t[self.rear]=(now.hour, now.minute, now.second)
#         self.rear=(self.rear+1)%self.cap
#         self.size=self.size+1
#     def dequeue(self):
#         if self.isempty():
#             print("Queue is empty")
#         self.que[self.front]=None
#         self.front=(self.front+1)%self.cap
#         self.size=self.size-1
#     def isfull(self):
#         return self.size==self.cap
#     def isempty(self):
#         return self.size==0
#     def display(self):
#         return self.que
#
# obj=Queue(5)
# for i in range(9):
#     obj.enqueue(i)
# print(obj.display())