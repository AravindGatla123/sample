for i in range(4):
    for j in range(4):
        print("#", end="")
    j = j + 1
    print("#")


class Car:

    def __init__(self, transmission, front_wheel, rare_wheel):
        self.transmission = transmission
        self.front_wheel = front_wheel
        
        self.rare_wheel = rare_wheel

    def features(self):
        print("feature:", self.transmission, self.front_wheel, self.rare_wheel)
    def compare(self,other):
        if Audi.transmission == other.transmission:
            return True
        else:
            return False


Audi = Car("manual", "yes", "no")
Dodge = Car("Auto", "no", "yes")
if Audi.compare(Dodge):
    print("they are same")
else:
    print("they are different")

