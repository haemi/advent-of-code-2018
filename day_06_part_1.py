import numpy as np
import operator
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

for index, x in np.ndenumerate(matrix):
    if index[0] < min_x or index[1] < min_y:
        continue

    if x > 0:
        continue

    currently_closest_distance = 999999
    currently_closest_point = points[0]

    clearly_nearest_point = False

    for point in points:
        current_distance = abs(point[0] - index[0]) + abs(point[1] - index[1])

        if current_distance == currently_closest_distance:
            clearly_nearest_point = False
        elif current_distance < currently_closest_distance:
            clearly_nearest_point = True
            currently_closest_point = point
            currently_closest_distance = current_distance

    if clearly_nearest_point:
        matrix[index] = currently_closest_point[2]

# first row
for entry in matrix[0]:
    matrix[matrix == entry] = 0

# last row
for entry in matrix[matrix.shape[0]-1]:
    matrix[matrix == entry] = 0

# first column
for entry in matrix.T[0]:
    matrix[matrix == entry] = 0

# last column
for entry in matrix.T[matrix.shape[1]-1]:
    matrix[matrix == entry] = 0

matrix = matrix.astype(int)
matrix_list = matrix.tolist()
unique, counts = np.unique(matrix_list, return_counts=True)
counts = dict(zip(unique, counts))
print(sorted(counts.items(), key=operator.itemgetter(1), reverse=True)[1][1], 'execution time: {:.2f} seconds'.format(time.time() - start))
