# a program that explains getter and setter

class Square:
    def __init__(self, size):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if not isinstance(size, (int, float)):
            raise TypeError("size must be an integer or float")
        elif size < 0:
            raise ValueError("size must be >= 0 ")
        else:
            self.__size = size

square = Square(10)
print(square.size)