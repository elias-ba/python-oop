import random


class Player:
    def __init__(self, name, skill_rate=50):
        self.name = name
        self.skill_rate = skill_rate
        self.__score = 0

    def score(self):
        self.__score += 1

    def reset_score(self):
        self.__score = 0

    def get_score(self):
        return self.__score

    def shoot(self):
        ball = Ball()
        ball.set_speed(self.skill_rate)
        return ball

    def intercept(self, ball):
        intercept_chance = self.skill_rate * \
            random.uniform(0, 1) - ball.get_speed() * 0.01
        return intercept_chance > 0


class Ball:
    def __init__(self):
        self.__speed = random.uniform(0, 50)

    def set_speed(self, player_skill_rate):
        self.__speed += 50 * player_skill_rate**2

    def get_speed(self):
        return self.__speed
