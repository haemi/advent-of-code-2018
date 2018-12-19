import time
from aocd import get_data
from aocd import submit

start = time.time()

lines_8 = list(map(int, get_data(day=8).split(' ')))


def parse_node(meta_data, numbers):
    amount_of_child_nodes = numbers.pop(0)
    amount_of_meta_data_nodes = numbers.pop(0)
    for node_index in range(0, amount_of_child_nodes):
        meta_data = parse_node(meta_data, numbers)
    for meta_data_index in range(0, amount_of_meta_data_nodes):
        meta_data += numbers.pop(0)
    return meta_data


my_solution = parse_node(0, lines_8)

print('execution time: {:.2f} seconds'.format(time.time() - start))

submit(my_solution, level=1, day=8, year=2018)
