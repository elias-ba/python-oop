import abc
import math


class Shape(metaclass=abc.ABCMeta):
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


class ShapeFactory:

    known_shapes = ['rectangle', 'circle', 'square']

    def is_known_shape(self, shape_name):
        return shape_name in self.known_shapes

    def create_shape(self, shape_name='circle'):
        if shape_name == 'circle':
            radius = input(
                "What is the radius of your circle (in centimeters)? : ")
            return Circle(float(radius))

        elif shape_name == 'rectangle':
            height = input(
                "What is the height of your rectangle (in centimeters)? : ")
            width = input(
                "What is the width of your rectangle (in centimeters)? : ")
            return Rectangle(h=float(height), w=float(width))

        elif shape_name == 'square':
            width = input(
                "What is the width of your square (in centimeters)? : ")
            return Square(w=float(width))

        else:
            return None
