# class attributes and instance attributes

class Circle:
    PI = 2
    def __init__(self, radius):
        self.radius = radius
        self.diameter = 2 * radius

    @property
    def circumference(self):
        return 2 * Circle.PI * self.radius
    

circle1 = Circle(4)

print(circle1.circumference)

Circle.PI = 4

print(circle1.circumference)
