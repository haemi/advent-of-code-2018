import time
from aocd import get_data
from aocd import submit
import numpy as np
import itertools
from skimage.util.shape import view_as_windows

lines_11 = get_data(day=11)


def calculate_power_level(coordinate, serial_number=int(lines_11)):
    x = coordinate[0]
    y = coordinate[1]

    rack_id = x + 10
    power_level = rack_id * y
    power_level += serial_number
    power_level *= rack_id
    power_level = int((power_level / 100) % 10)
    power_level = power_level - 5
    return power_level


def find_coordinate_of_most_power(serial_number=int(lines_11)):
    coordinates = itertools.product(range(1, 301), range(1, 301))
    power_levels = [calculate_power_level(c, serial_number) for c in coordinates]

    power_levels_np = np.asarray(power_levels).reshape(300, 300)

    highest_power = 0
    upper_left_x = 0
    upper_left_y = 0
    square_size = 0

    for sq_si in range(1, 301):
        windows = view_as_windows(power_levels_np, (sq_si, sq_si))
        for x in range(0, windows.shape[0]):
            for y in range(0, windows.shape[1]):
                window_sum = windows[x, y].sum()
                if window_sum > highest_power:
                    highest_power = window_sum
                    upper_left_x = x + 1
                    upper_left_y = y + 1
                    square_size = sq_si

    return '{},{},{}'.format(upper_left_x, upper_left_y, square_size)


# print('1')
# assert(calculate_power_level((3, 5), 8) == 4)
# print('2')
# assert(calculate_power_level((122, 79), 57) == -5)
# print('3')
# assert(calculate_power_level((217, 196), 39) == 0)
# assert(calculate_power_level((101, 153), 71) == 4)
# print('5')
# assert(find_coordinate_of_most_power(18) == '90,269,16')
# print('6')
# assert(find_coordinate_of_most_power(42) == '232,251,12')
# print('7')

start = time.time()

my_solution = find_coordinate_of_most_power()
print('{}, execution time: {:.2f} seconds'.format(my_solution, time.time() - start))
submit(my_solution, level=2, day=11, year=2018)
