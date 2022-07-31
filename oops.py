# class - design - blue print
# object- instance
# Attributes- variable.py(instance variable[in side init function], class(static variable- out side init)
# Behaviour- Methods(functions)
# Special varibale = _name_
# Special method = _init_


class Computer:

    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print("config is :", self.cpu, self.ram)


com1 = Computer('I5', 8)
com2 = Computer('M1', 16)

# Call with class and method
com1.config()  # calling method with  obj
com2.config()  # calling method with  obj


class People:

    def __int__(self):
        self.name = "Aravind"
        self.age = 25


c1 = People()
c2 = People()


print(c1.age)
