import abc
import math


class Shape(    ):
    @abc.abstractmethod
    def calculate_perimeter(self):
        pass

    @abc.abstractmethod
    def calculate_area(self):
        pass


class Rectangle(Shape):
    def __init__(self, h, w):
        self.height = h
        self.width = w

    def calculate_perimeter(self):
        return 2 * (self.height + self.width)

    def calculate_area(self):
        return self.height * self.width


class Square(Shape):
    def __init__(self, w):
        self.width = w

    def calculate_perimeter(self):
        return 4 * self.width

    def calculate_area(self):
        return self.width ** 2


class Circle(Shape):
    def __init__(self, r):
        self.radius = r

    def calculate_perimeter(self):
        return 2 * math.pi * self.radius

    def calculate_area(self):
        return math.pi * (self.radius ** 2)


if __name__ == "__main__":
    shape_name = input(
        "What is the name of the shape (rectangle, cirlce, or square)? : ")
    if shape_name == 'circle':
        radius = input(
            "What is the radius of your circle (in centimeters)? : ")
        circle = Circle(float(radius))
        print(
            f"Your circle's perimeter is {circle.calculate_perimeter()} cm and it's area is {circle.calculate_area()} cm2")

    elif shape_name == 'rectangle':
        height = input(
            "What is the height of your rectangle (in centimeters)? : ")
        width = input(
            "What is the width of your rectangle (in centimeters)? : ")
        rectangle = Rectangle(h=float(height), w=float(width))
        print(
            f"Your rectangle's perimeter is {rectangle.calculate_perimeter()} cm and it's area is {rectangle.calculate_area()} cm2")

    elif shape_name == 'square':
        width = input(
            "What is the width of your square (in centimeters)? : ")
        square = Square(w=float(width))
        print(
            f"Your square's perimeter is {square.calculate_perimeter()} cm and it's area is {square.calculate_area()} cm2")
    else:
        print("Unknown shape, please make sure you give the values : rectangle, square, or circle.")
