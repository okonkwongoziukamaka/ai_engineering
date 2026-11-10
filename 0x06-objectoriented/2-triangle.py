# a program to calculate the area of a triangle 

class Triangle:
    def __init__(self, height, breath):
        self.height = height
        self.breath = breath
    def area(self):
        return(0.5 * self.height*self.breath)
    
triangle = Triangle(20, 25)
print(triangle.area()) 