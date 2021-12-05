"""Create a Rectangle class whose attributes will be the height and width of
the figure. Implement methods to measure the perimeter and area of a
rectangle.
Then create a Square class, remembering that every square is a
rectangle, but not every rectangle is a square"""


class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def perimeter(self):
        return (self.height + self.width)*2

    def area(self):
        return self.height * self.width

if __name__ == "__main__":


    r = Rectangle(3, 4)
    print("staciak perimetras ", r.perimeter())
    print("staciak plotas " , r.area())


class Square(Rectangle):

    def __init__(self, line_width):
        self.line_width = line_width

    def perimeter(self):
        return self.line_width*4

    def area(self):
        return self.line_width**2

if __name__ == "__main__":
    s = Square(5)
    print("kvadrato perimetras ", s.perimeter())
    print("kvadrato plotas", s.area())
