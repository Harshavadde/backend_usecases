import threading
import time

class Transaction:
    def __init__(self):
        self.db = {
            'student1': {'sid': 101, 'sname': 'harsha', 'bal':100},
            'student2': {'sid': 102, 'sname': 'karthik', 'bal': 100},
            'student3': {'sid': 103, 'sname': 'mahesh', 'bal': 75}
        }
        self.stack = []
        self.lock = threading.Lock()
    def create(self, user):
        if self.read(user) in self.stack:
            self.stack.remove(self.read(user))
        if user not in self.db:
            self.db[user] = {}
            self.db[user]['sid'] = int(input("Enter student id: "))
            self.db[user]['sname'] = input("Enter student name: ")
            self.db[user]['bal'] = int(input("Enter student bal: "))
            print()
            self.add(user)
        else:
            print("user is already exist:")
            return

    def select(self, user):
        if user not in self.db:
            print("user does not exist")
            return
        return self.db[user]
    def update(self, user,bal):
        self.db[user]['bal'] = bal
        print("wait for 5 seconds:")
        time.sleep(5)

    def withdraw(self, user):
        with self.lock:
            if self.select(user) not in self.stack:
                print("user does not exist in stack")
                return
            wamt = int(input("Enter student bal: "))
            for i in self.stack:
                if i == self.select(user):
                    if i['bal'] < wamt:
                        print("student bal is less than wamt")
                        return
                    i['bal'] = i['bal'] - wamt
                    u_b = i['bal']
                    print("updated balance",u_b)
        self.update(user,u_b)



    def delete(self, user):
        if user not in self.stack:
            print("user does not exist")
            return
        self.stack.remove(self.db[user])
        self.stack.pop()

    def add(self, user):
        if user not in self.db:
            print("user does not exist")
            return
        self.stack.append(self.select(user))
    def display(self):
        print(self.stack)
        print(self.db)

obj = Transaction()
obj.add('student1')
obj.add('student2')
obj.add('student3')
# obj.withdraw('student1')
obj.display()
t1 = threading.Thread(target=obj.withdraw, args=("student1",))
t2 = threading.Thread(target=obj.withdraw, args=("student1",))
t1.start()
t2.start()
t1.join()
t2.join()
obj.display()
# obj.update("student2")