class Node:
    def __init__(self,key,val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class doubly_linkedlist:
    def __init__(self):
        self.head=None
        self.tail=None

    def push(self,key,val):
        new = Node(key,val)
        if self.head is None:
            self.head = new
            self.tail = new
            return
        new.next = self.head
        self.head.prev = new
        self.head = new
    def pop(self):
        if self.head is None:
            return None
        temp = self.head
        self.head = self.head.next
        temp.prev = None
        return temp
    def display(self):
        if self.head is None:
            return None
        temp = self.head
        while temp:
            print(temp.key)
            print(temp.val)
            temp = temp.next

class stack(doubly_linkedlist):
    def __init__(self):
        self.db={0:[],1:[]}
        self.count=0
        super().__init__()
    def push(self,key,value):
        super().push(key,value)
        # self.db[key]=value
        if self.count == 0:
            self.db[0].append((key,value))
        elif self.count == 1:
            self.db[1].append((key,value))
        elif self.count == 2:
            self.db[0].append((key,value))
        else:
            self.db[key]=value

        self.count += 1
    def pop(self):
        temp=super().pop()
        self.db.pop(temp)
    def display1(self):
        return self.db

obj=stack()
obj.push(101,"men")
obj.push(102,"women")
obj.push(103,"child")
# obj.push("Byee",104)
# obj.push("Byeee",105)
print(obj.display1())