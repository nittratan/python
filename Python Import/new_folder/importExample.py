# person class
class Person:
    def __init__(self, id , name, age):
        self.id = id
        self.name = name
        self.age = age

    def display(self):
        print("Id: ", self.id)
        print("Name: ", self.name)
        print("Age: ", self.age)

# p = Person(1, "Ratan Sharma", 24)

# p.display()