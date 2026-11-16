# a program that utilise break and continue

items = ["mango", "Apple", "Banana", "Gwava", "Watermelon"]

for item in items:
    if item == "Banana":
        break
    print(item)


for i in range(1, 11):
    if i == 5:
        continue
    print(i)

for i in range(1, 10):
    if i == 5:
        break
    print(i)

    