import time
from aocd import get_data

start = time.time()

lines_1 = list(map(int, get_data(day=1).split('\n')))


def part2():
    values_visited = set()
    current_value = 0

    while True:
        for intValue in lines_1:
            current_value += intValue

            if current_value in values_visited:
                print(current_value, 'execution time: {:.2f} seconds'.format(time.time() - start))
                return

            values_visited.add(current_value)


part2()
