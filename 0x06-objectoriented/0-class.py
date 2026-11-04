# a program that explains object oriented programming

class Person:
    name = None
    __password = None
    age = 0

person = Person()
person.name = "Favour"
person.age = 32

print(dir(person))
print(person.__dict__)
print(person.name)
print(person.age)
print(person)