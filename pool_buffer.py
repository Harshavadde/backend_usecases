import time
class Database:
    def __init__(self):
        self.db = {
            'student1' : {'sid':101,'sname':'harsha','marks':60},
            'student2' : {'sid':102,'sname':'karthik','marks':65},
            'student3' : {'sid':103,'sname':'mahesh','marks':75}
        }
        self.stack = []

    def create(self,user):
        if self.read(user) in self.stack:
            self.stack.remove(self.read(user))
        if user not in self.db:
            self.db[user] = {}
            self.db[user]['sid'] = int(input("Enter student id: "))
            self.db[user]['sname'] = input("Enter student name: ")
            self.db[user]['marks'] = int(input("Enter student marks: "))
            self.read(user)
        else:
            print("user is already exist:")
            return

    def read(self,user):
        if user not in self.db:
            print("user does not exist")
            return
        l=[]
        for i in self.db[user].values():
            l.append(i)
        self.stack.append(l)
        return l


    def update(self,user):
        if user not in self.db:
            print("user does not exist")
            return
        else:
            self.db[user]['sid'] = int(input("Enter student id: "))
            self.db[user]['sname'] = input("Enter student name: ")
            self.db[user]['marks'] = int(input("Enter student marks: "))
            if self.read(user) not in self.stack:
                self.read(self.db[user]["sid"])

    def delete(self,user):
        if user not in self.stack:
            print("user does not exist")
            return
        if self.read(user) in self.stack:
            self.stack.remove(self.read(user))
        x=self.stack.remove(self.read(user))
        if x==self.read(user):
            self.db.pop(user)



    def display(self):
        print(self.db)
        # print(self.stack)

obj = Database()
# obj.create("student1")
# obj.delete("student1")
# obj.update("student2")
obj.read("student3")
obj.display()
