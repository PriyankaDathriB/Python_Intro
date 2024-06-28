class Student:
    def __init__(self,n,r,a):
        self.name = n
        self.roll_no = r
        self.addr = a

    def display(self):
        print(self.name)

s1 = Student("Pravalika",32,"bklore")
s1.display()
s2 = Student("Pra",321,"bksdslore")
s2.display()
