import time
from aocd import get_data
from aocd import submit
from collections import deque

lines_9 = get_data(day=9)


def calculate_highscore(players, last_marble):
    highscore = []
    for player in range(0, players):
        highscore.append(0)

    placed_marbles = deque([0])

    for marble_index in range(1, last_marble + 1):
        current_player = marble_index % players

        if marble_index % 23 == 0:
            highscore[current_player] += marble_index
            placed_marbles.rotate(7)
            highscore[current_player] += placed_marbles.pop()
            placed_marbles.rotate(-1)
        else:
            placed_marbles.rotate(-1)
            placed_marbles.append(marble_index)

    return max(highscore)


assert(calculate_highscore(9, 25) == 32)
assert(calculate_highscore(10, 1618) == 8317)
assert(calculate_highscore(13, 7999) == 146373)
assert(calculate_highscore(17, 1104) == 2764)
assert(calculate_highscore(21, 6111) == 54718)
assert(calculate_highscore(30, 5807) == 37305)

start = time.time()

numbers = [int(s) for s in lines_9.split() if s.isdigit()]
my_solution = calculate_highscore(numbers[0], numbers[1] * 100)
print('{}, execution time: {:.2f} seconds'.format(my_solution, time.time() - start))
submit(my_solution, level=2, day=9, year=2018)
