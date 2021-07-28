class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)

        self.breed = breed

    def bark(self):
        print(f'Dog named {self.name} is barking')

class Cat(Animal):
    def meow(self):
        print(f"{self.name} says meow")

class Frog(Animal):
    def eat(self):
        print(f"Frog with name {self.name} is eating")

d = Dog("Sharik", "terier")
c = Cat("Snejiok")
f = Frog("Froggy")

f.eat()
print(f.name)