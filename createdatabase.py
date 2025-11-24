class database:
    def __init__(self):
        self.db = {}
        self.count=1
    def insert(self,record):
        pk=self.count
        self.db[pk]=record
        self.count += 1

    def delete(self,key):
        if key in self.db:
             del self.db[key]
    def update(self,key,val):
        if key in self.db:
            self.db[key]=val

    def select(self):
        return self.db

lst=["hi",12,"db"]
obj = database()
print(obj.insert(lst))
print(obj.select())
# print(obj.insert())
lst2=["hii",34,"db1"]
print(obj.insert(lst2))
print(obj.select())

