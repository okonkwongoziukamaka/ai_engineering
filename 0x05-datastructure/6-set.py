# a program that explains sets and its operation

number = {1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5}
print(number)
number.add(6)
number.add(7)
print(number)
number.remove(3)
print(number)
a = {1, 2, 3, 4}
b = {3, 4, 5}
aub = a.union(b)
print(aub)
anb = a.intersection(b)
print(anb)
asb = a.symmetric_difference(b)
print(asb)
adb = a.isdisjoint(b)
print(adb)