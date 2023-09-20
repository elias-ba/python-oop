from models import Player, Ball

player_a = Player(name="Amadou", skill_rate=.75)
player_b = Player(name="Samba", skill_rate=.95)

__SETS__ = 50
__MATCHES__ = 25

for match in range(__MATCHES__):
    a_misses, b_misses = 0, 0
    player_a.reset_score()
    player_b.reset_score()
    while a_misses < __SETS__ and b_misses < __SETS__:
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

    print(
        f"The winner of match number {match + 1} is {winner.name} with a score of {winner.get_score()}")
