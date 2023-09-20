from models import Player, Ball

player_a = Player(name="Amadou", skill_rate=60)
player_b = Player(name="Samba", skill_rate=78)

a_misses, b_misses = 0, 0
while a_misses < 5 and b_misses < 5:
    ball = player_a.shoot()
    b_did_intercept = player_b.intercept(ball)

    if not b_did_intercept:
        player_a.score()
        b_misses += 1

    ball = player_b.shoot()
    a_did_intercept = player_a.intercept(ball)

    if not a_did_intercept:
        player_b.score()
        a_misses += 1

winner = player_b if a_misses > b_misses else player_a

print(f"The winner is {winner.name} with a score of {winner.get_score()}")
