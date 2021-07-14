class Car:
    def __init__ (self,name,energy1):
       self.name = name
       self.energy1 = energy1

    def drive(self):
        print(self.name + " speed up!")
    
class Hybrid_Car(Car):
    def __init__ (self,name,energy1,energy2):
        super().__init__(name,energy1)
        self.energy2 = energy2

a = input()
b = input()
c = input()

old_car = Car(a,b)
toyota = Hybrid_Car(a,b,c)
print(old_car.energy1)
print(toyota.energy2)
toyota.drive()