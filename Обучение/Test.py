a = 'hello'
a = a.upper()
#print(a)


class Car:
    def __init__(self, colour=None, brand=None, model=None):
        self.colour = colour
        self.brand = brand
        self.model = model

    def honk(self):
        print(f'{self.brand} {self.model} honks')


car1 = Car('blue', 'Mazda', 'RX-8')
car1.honk()