import time
import operator
from aocd import get_data
# from aocd import submit

lines_15 = get_data(day=15).split('\n')

start = time.time()

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Element:
    def __init__(self, point, character):
        self.point = point
        self.character = character

    def make_turn(self):
        if self.character not in ['E', 'G']:
            print('ouch!')
            return
        print('making turns')


elements = []

for y, line in enumerate(lines_15):
    for x, character in enumerate(list(line)):
        elements.append(Element(Point(x, y), character))

while True:
    units = filter(lambda x: x.character == 'G' or x.character == 'E', elements)
    for unit in sorted((x for x in units), key=lambda iter_unit: (iter_unit.point.y, iter_unit.point.x)):
        unit.make_turn()
    break


print(lines_15)

result = ''

print('{}, execution time: {:.2f} seconds'.format(result, time.time() - start))
# submit(result, level=1, day=15, year=2018)
