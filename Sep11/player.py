class Player:
    def __init__(self, name, number, age, nationality, speed, club):
        self.number = number
        self.name = name
        self.age = age
        self.nationality = nationality
        self.speed = speed
        self.current_club = club

    def run(self):
        print(f"Running at a speed of {self.speed} KM/Hr")

    def kick(self):
        print(f"Kicking the ball very hard ...")

    def intro(self):
        print(f"I am {self.name}, I wear the number {self.number}. I am {self.age} years old and from {self.nationality}. I run {self.speed} KM/Hr. My club is {self.current_club}")
