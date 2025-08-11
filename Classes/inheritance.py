class Shape:

    def __init__(self, name, sides, color):
        self.name = name
        self.sides = sides
        self.color = color

    def describe(self):
        print(f"This shape is called {self.name}, it has {self.sides} sides, and the color is {self.color}")


# Subclass Rectangle
class Rectangle(Shape):
    def __init__(self, width, length, color="dark green"):
        super().__init__(name="rectangle", sides=4, color=color)
        self.width = width
        self.length = length

    def area(self):
        a = self.width * self.length
        print(f"For {self.name},of side {self.sides}, has an area of {a}")
        return a


# Create objects
shape1 = Shape(name="circle", sides=0, color="pink")
shape2 = Shape(name="triangle", sides=3, color="violet")
rect = Rectangle(width=5, length=3)  # width and length are required

# Describe 
shape1.describe()
shape2.describe()
rect.describe()

rect.area()
