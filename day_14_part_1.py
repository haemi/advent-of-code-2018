import time
from aocd import get_data
from aocd import submit
from collections import deque

lines_14 = int(get_data(day=14))

start = time.time()

circle = deque([3, 7])

first_index = 0
second_index = 1

stop_after = int(get_data(day=14))

while True:
    first_score = circle[first_index]
    second_score = circle[second_index]
    final_score = first_score + second_score
    final_score_splitted = [int(i) for i in str(final_score)]
    circle.extend(final_score_splitted)
    first_index = (first_score + first_index + 1) % len(circle)
    second_index = (second_score + second_index + 1) % len(circle)

    if len(circle) >= stop_after + 10:
        print(circle)
        print(''.join(list(map(lambda x: str(x), list(circle)[stop_after:stop_after+10]))))
        break

result = ''.join(list(map(lambda x: str(x), list(circle)[stop_after:stop_after+10])))
print('{}, execution time: {:.2f} seconds'.format(result, time.time() - start))
submit(result, level=1, day=14, year=2018)
