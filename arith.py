def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def prod(a,b):
    return a*b

def div(a,b):
    return a/b

class Student:
    def __init__(self,n,r,a):
        self.name = n
        self.roll_no = r
        self.addr = a

    def display(self):
        print(self.name)