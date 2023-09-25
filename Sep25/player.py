class Player:

    number_instances = 0

    def __init__(self, name):
        if Player.number_instances >= 2:
            raise RuntimeError("You can't instantiate more than 2 players for a tennis game.")
        else:
            self.name = name
            Player.number_instances += 1
