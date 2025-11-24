import numpy as np
import math
class vector:
    def __init__(self,x,y):
        self.db1={}
        self.db2={}
        self.auto=1
        self.auto2=1
        self.v1 = []
        self.v2 = []

        with open(x,"r") as fp:
            reader = fp.read()
            # print(reader)
            for i in reader.split():
                self.db1[self.auto]=i
                self.auto+=1
        with open(y,"r") as fp1:
            reader1 = fp1.read()
            # print(reader1)
            for j in reader1.split():
                self.db2[self.auto2]=j
                self.auto2+=1

    def create_vector(self):
        self.v1=[]
        self.v2=[]
        for i in range(1,len(self.db1)+1):
            if self.db1.get(i)==self.db2.get(i):
                self.v1.append(1)
            else:
                self.v1.append(0)
        for j in range(1,len(self.db2)+1):
            if self.db2.get(j)==self.db1.get(j):
                self.v2.append(1)
            else:
                self.v2.append(0)
    def dot_product(self,v1,v2):
        s=0
        for i,j in zip(v1,v2):
            s+=i*j
        return s
    def magnitude(self,n):
        s=0
        for x in n:
            s+=x*x
        return math.sqrt(s)
    def cosine_angle(self,v1,v2):
        dot = self.dot_product(v1,v2)
        print("dot product",dot)
        m1 = int(self.magnitude(self.v1))
        m2 = int(self.magnitude(self.v2))
        if m1==0 or m2==0:
            return False
        cos = dot//(m1*m2)
        print("cos theta=",cos)
        if cos<1:
            return False
        else:
            return True

    def display(self):
        print(self.db1)
        print("="*50)
        print(self.db2)
    def display2(self):
        print(self.v1)
        print(self.v2)

obj = vector("doc1.data","doc2.data")
obj.display()
obj.create_vector()
obj.display2()
print(obj.cosine_angle(obj.v1,obj.v2))