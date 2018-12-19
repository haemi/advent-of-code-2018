import numpy as np
import time
from aocd import get_data

start = time.time()

lines_6 = get_data(day=6).split('\n')

points = []

point_index = 0

for line in lines_6:
    x = int(line.split(',')[0])
    y = int(line.split(',')[1])
    point_index += 1
    points.append((x, y, point_index))

min_x = 999999
min_y = 999999
max_x = 0
max_y = 0

for point in points:
    min_x = min(min_x, point[0])
    min_y = min(min_y, point[1])
    max_x = max(max_x, point[0])
    max_y = max(max_y, point[1])

matrix = np.zeros((max_x + 1, max_y + 1))

for point in points:
    matrix[point[0], point[1]] = point[2]

matrix = matrix.T

limit = 10000

for index, x in np.ndenumerate(matrix):
    distance_sum = 0

    for point in points:
        distance_sum += abs(point[0] - index[0]) + abs(point[1] - index[1])

        if distance_sum >= limit:
            break

    if distance_sum < limit:
        matrix[index] = 100

print((matrix >= 100).sum(), 'execution time: {:.2f} seconds'.format(time.time() - start))
