class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Person created")

    def say_hello(self):
        print(f"{self.name} say hello!")


class Student(Person):
    def __init__(self, name, age, average_grade):
        #Person.__init__(self, name, age)
        super().__init__(name, age)

        self.average_grade = average_grade
        print("Student created")

    def study(self):
        print(f"{self.name} studies")

    def say_hello(self):
        super().say_hello()
        print(f"Student with name: {self.name} say hello!")

class Teacher(Person):
    pass

def introduce(person):
    print("Now, a person will say hello")
    person.say_hello()

people_qrr = [Student("Tom", 18, 3.5), Teacher("Katy", 45), Student("Bob", 26, 4.8)]\

for person in people_qrr:
    introduce(person)