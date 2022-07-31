# instance method- accessor, mutator
#static method
#class method

class student:
    school = "midland"

    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
    def avg(self):
        return (self.m1 + self.m2 + self.m3)/3

    @classmethod

    def get_school_name(cls):
        return cls.school

    @staticmethod
    def info():
        print("This is a static method")


s1 = student(34,43,54)
s2 = student(44,53,64)
if s2.avg() > s1.avg():
    print("S2 is smart")
else:
    print("S1 is smart")
print(student.get_school_name())
student.info()

