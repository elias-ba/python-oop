from player import Player

if __name__ == "__main__":
    sadio = Player(name="Sadio", number=10, age=31, speed=5,
                   club="Al Nassr", nationality="SN")
    ismaila = Player(name="Ismaila", number=18, age=25,
                     speed=7, club="Marseille", nationality="SN")
    
    for player in [sadio, ismaila]:    
        player.intro()
        print("---")
        player.run()
        print("---")
        player.kick()
        print("--------------------")
