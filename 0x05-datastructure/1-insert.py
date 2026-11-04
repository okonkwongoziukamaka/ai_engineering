# a program that can an item anywhere in the list without using append

car = []
car.append("Camry")
car.append("bus")
car.append("Gwagon")

print(car)
car.insert(0, "Toyota")
print(car)
car.insert(2, "Jeep")
print(car)
car.pop()
car.pop(2)
print(car)
