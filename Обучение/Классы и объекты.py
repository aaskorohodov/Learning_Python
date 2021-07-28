class Person:
    some_num = 123
    counter = 0
    def __init__(self, name, surname, place_of_birth, year_of_birth):
        self.name = name
        self.surname = surname
        self.place_of_birth = place_of_birth
        self.year_of_birth = year_of_birth
        Person.counter += 1

    def print_info(self, n):
        for i in range(n):
            print(
                  f"Name: {self.name}"
                  f"Surname: {self.surname}"
                  f"Place Of Birth: {self.place_of_birth}"
                  )
    def get_age(self, n):
        print(f"Возраст: {2020 - int(self.year_of_birth)}")

p1 = Person("Elon", "Musk", "ЮАР", "1971")
p2 = Person("Sergei", "Korolev", "Российская Империя", "1907")
p3 = Person("Albert", "Einstein", "Германия", "1879")

p3.get_age(2021)
Person.print_info(p3, 1)
p1.print_info(1)
p2.print_info(1)
p3.print_info(1)

Person.some_num = 456

print(p1.some_num)
print(Person.some_num)

class Circle:

    PI = 3.14

    def __init__(self, radius):
        self.radius = radius
    def get_perimetr(self):
        return self.radius * 2 * self.PI
    def get_area(self):
        return Circle.PI * self.radius ** 2

c1 = Circle(3)
print(c1.get_perimetr())
print(c1.get_area())

c2 = Circle(7)
print(c2.get_perimetr())
print(c2.get_area())

print(Person.counter)