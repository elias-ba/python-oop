class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def shout(self, message="I am a weird pet"):
        print(message)


class Dog(Pet):
    def __init__(self, name, age, species):
        super().__init__(name, age)
        self.species = species

    def shout(self):
        message = f"I am {self.name} the dog, I am {self.age} years old, and I am {self.species}"
        super().shout(message)


class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def shout(self):
        message = f"I am {self.name} the cat, I am {self.age} years old, and I am of a {self.color} color"
        super().shout(message)


pets = [Dog("Ricky", 2, "canny"), Cat(
    "Garfield", 3, "brown"), Pet("My Weird Pet", 40)]
for pet in pets:
    pet.shout()
