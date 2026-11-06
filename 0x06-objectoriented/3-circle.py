

class Circle:
    def __init__(self, radius):
         self.radius = radius

    def area(self):
         return(3.143 * self.radius**2)

circle = Circle(50)
print(circle.area())
    