import threading
import time
import datetime
class semaphore:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def sumop(self,a,b):
        print(self.a + self.b)

    def multiply(self,a,b):
        print(self.a * self.b)

    def display(self,x):
        start = datetime.datetime.now().second
        print("execution starting time:",start)
        thread = threading.Thread(target=x,args=(start,))
        time.sleep(6)
        end = datetime.datetime.now().second
        print("execution ending time:",end)
        if (end-start) < 10:
            return True
        return False


obj = semaphore(5,6)
# obj.sumop(5,6)
print(obj.display(obj.sumop(5,6)))