class Queue:
    def __init__(self,a):
        self.que=[0]*a
        self.front=0
        # self.front_que=0
        self.rear=0
        # self.rear_que=0
        self.capacity = a
        self.size = 0
    def enque(self,val):
        self.start = time.time()
        if self.isfull():
            print("Queue is full")
            return
        self.que[self.rear]=val
        self.rear = (self.rear+1)%self.capacity
        self.size+=1
        self.end = time.time()
    def deque(self):
        if self.isempty():
            return -1
        self.que.pop([self.front])
        self.size -=1
    def isempty(self):
        if not self.que:
            return True
    def isfull(self):
        return self.size == self.capacity
    def length(self):
        return self.size
    def display(self):
        return self.que

obj = Queue(10)
for i in [10,20,30,40,50]:
    obj.enque(i)
print(obj.display())

