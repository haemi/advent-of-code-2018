import time
from aocd import get_data
from aocd import submit
import re
import sys

lines_10 = get_data(day=10).split('\n')

start = time.time()


class Dot(object):
    def __init__(self, x, y, vel_x, vel_y):
        super(Dot, self).__init__()
        self.x = x
        self.y = y
        self.vel_x = vel_x
        self.vel_y = vel_y

    def advance(self):
        self.x += self.vel_x
        self.y += self.vel_y

    def __repr__(self):
        return 'x: {}, y: {}'.format(self.x, self.y)

    def __copy__(self):
        newone = type(self)()
        newone.x = self.x
        newone.y = self.y
        return newone


dots = set()

for line in lines_10:
    entry = [int(s) for s in re.findall(r'-?\d+', line)]
    dots.add(Dot(entry[0], entry[1], entry[2], entry[3]))

min_area = sys.maxsize

iterations_without_new_min = 0
i = 0
current_seconds = 0

while True:
    i += 1

    [dot.advance() for dot in dots]

    min_x = min(map(lambda dot: dot.x, dots))
    max_x = max(map(lambda dot: dot.x, dots))
    min_y = min(map(lambda dot: dot.y, dots))
    max_y = max(map(lambda dot: dot.y, dots))

    temp_min_width = abs(max_x - min_x)
    temp_min_height = abs(max_y - min_y)

    if iterations_without_new_min > 1000:
        break

    if temp_min_width * temp_min_height < min_area:
        iterations_without_new_min = 0
        min_area = temp_min_width * temp_min_height
        current_seconds = i
    else:
        iterations_without_new_min += 1


my_solution = current_seconds
print('{}, execution time: {:.2f} seconds'.format(my_solution, time.time() - start))
submit(my_solution, level=2, day=10, year=2018)
