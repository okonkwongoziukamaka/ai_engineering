# a program that use context manager to open a file

with open("Hello.txt", encoding = "utf-8") as file:
    print(file.read())