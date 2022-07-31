# duck typing, operator overloading, method overloading, method overriding
#polymoephism= many types
class Pycharm:

    def execute(self):
        print("compiling")
        print("done")

class eclipes:

    def execute(self):
        print("compiling")
        print("done")
        print("spell check")
        print("font")

class Laptop:

    def code(self,ide):
        ide.execute()

ide = eclipes()

lap1 = Laptop()
lap1.code(ide)


#operator overloading
class Student:

    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = Student(m1,m2)

        return s3

    def __sub__(self, other):
        m1 = self.m1 - other.m1
        m2 = self.m2 - other.m2
        s3 = Student(m1,m2)

        return s3

    def __gt__ (self, other):
        r1 = self.m1 + self.m1
        r2 = other.m2 + other.m2
        if r1 > r2:
            return True
        else:
            return False

    def __str__(self):
        return '{}  {} '.format(self.m1, self.m2)


s1 = Student(43,53)
s2 = Student(63,52)
s3 = s1 - s2
print(s3.m2)
s3 = s1 + s2
if s1 > s2:
   print("s1 is greater")
else:
    print("s2 is geater")

print(s1)
print(s2)

