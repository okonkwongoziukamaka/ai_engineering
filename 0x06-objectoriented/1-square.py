# a program that calculates and print the area of a square

class Square:
    def __init__(self, size):
        self.size = size

    def __str__(self):
        return(f"This is a public instance attribute {self.size}")

    def area (self):
        return(self.size**2)

square = Square(25)
print(square.area())
