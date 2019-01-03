import time
from aocd import get_data
from aocd import submit

lines_14 = int(get_data(day=14))

start = time.time()

circle = [3, 7]

first_index = 0
second_index = 1

stop_after = int(get_data(day=14))

current_string = ''

search_for = get_data(day=14)
search_for = [int(i) for i in search_for]

result = 0

while True:
    first_score = circle[first_index]
    second_score = circle[second_index]
    final_score = first_score + second_score
    final_score_splitted = [int(i) for i in str(final_score)]
    circle.extend(final_score_splitted)
    first_index = (first_score + first_index + 1) % len(circle)
    second_index = (second_score + second_index + 1) % len(circle)

    if search_for == circle[-len(search_for):]:
        result = len(circle) - len(search_for)
        break

    if search_for == circle[-len(search_for) - 1:-1]:
        result = len(circle) - len(search_for) - 1
        break

print('{}, execution time: {:.2f} seconds'.format(result, time.time() - start))
submit(result, level=2, day=14, year=2018)
