# a program that can read a file, print the result on the sxreen and return the file does not exist if the file is not existing

try:
    with open("Filename.txt", encoding = "utf-8") as file:
        print(file.read())
except FileNotFoundError:
    print("File not found Error")


