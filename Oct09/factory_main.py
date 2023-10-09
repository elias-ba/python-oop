from factory import ShapeFactory

if __name__ == "__main__":
    shape_name = input(
        "What is the name of the shape (rectangle, cirlce, or square)? : ")
    factory = ShapeFactory()
    if factory.is_known_shape(shape_name):
        shape = factory.create_shape(shape_name)
        print(
            f"The shape is a {type(shape)} and it's area is {shape.calculate_area()} cm2 and it's perimeter is {shape.calculate_perimeter()} cm")
    else:
        print(
            "Unknown shape, please make sure you give the values : rectangle, square, or circle.")
