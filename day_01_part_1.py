import time
from aocd import get_data
from functools import reduce

start = time.time()

lines_1 = map(int, get_data(day=1).split('\n'))

current_value = reduce((lambda x, y: x + y), lines_1)

print(current_value, 'execution time: {:.2f} seconds'.format(time.time() - start))
