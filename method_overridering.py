#method_overloading
class Student:


    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2

    def sum(self, a= None, b = None, c= None):

        s = 0

        if a!= None and b!=None and c!= None:
            s = a+b+c
        elif a!=None and b!=None:
            s = a+b
        else:
            s = a
        return   s

s1 = Student(21,32)

print(s1.sum(2,3,))


#method_overloading

class A:

    def show(self):
        print("In A show")

class B(A):

    def show(self):
        print("In B show")

class C(A):

    pass

a1 = C()
b1 = B()
a1.show()
b1.show()