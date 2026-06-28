class Shape:
    def area(self):
        print("Shape area")
class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        print(3.14*self.radius*self.radius)


c = Circle(5)
c.area()