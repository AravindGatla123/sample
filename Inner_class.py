
class Student:

    def __init__(self,name,rollnum):
        self.name = name
        self.rollnum = rollnum
        self.lap = self.Laptop()

    def show(self):
        print(self.name,self.rollnum)
        self.lap.show()

    class Laptop:

        def __init__(self):
            self.brand = "hp"
            self.cpu = "i8"
            self.ram = "8GB"

        def show(self):
            print(self.brand, self.cpu, self.ram)


s1 = Student("Aravind", 12345)
s2 = Student("Mac", 54321)

s1.show()

