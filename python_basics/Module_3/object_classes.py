class Circle:
    def __init__(self, color = "red", radius = 3):
        self.radius = radius
        self.color = color

    def area(self):
        area = self.radius**2 * 3.14
        return area
    
    def addRadius(self, r):
        self.radius = self.radius + r
        return self.radius

class Rectangle:
    def __init__(self, color, width, height):
        self.color = color
        self.width = width
        self.height = height
    
    def area(self):
        area = self.width * self.height
        return area
    
    def perimeter(self):
        perimeter = (self.width + self.height) * 2
        return perimeter

rec1 = Rectangle("red", 2, 4)
print(rec1.area())
print(rec1.perimeter())

circle1 = Circle("blue", 3)
print(circle1.radius)
circle1.color = "red"
print(circle1.color)

circle1.addRadius(8)
print(circle1.radius)

print(dir(circle1))