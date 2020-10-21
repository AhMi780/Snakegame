class Animal:
    def __init__(self,name,color):
        self.name = name
        self.color = color

class Dog(Animal) :
    def bark(self):
        print("woof")

class Cat(Animal):
    def bark(self):
        print("purr")
        

mano = Cat('mano','White')

print(mano.name,mano.color)
mano.bark()

