import time
from aocd import get_data
from aocd import submit

start = time.time()

lines_8 = list(map(int, get_data(day=8).split(' ')))
# lines_8 = list(map(int, '2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2'.split(' ')))


class Node(object):
    def __init__(self, child_count, meta_data_count):
        super(Node, self).__init__()
        self.children = []
        self.meta_data = []
        self.parent: Node = None
        self.child_count = child_count
        self.meta_data_count = meta_data_count

    def __repr__(self):
        if self.parent is None:
            return '*{}-{}, parent: -, children: {}, meta_data: {}*'.format(self.child_count, self.meta_data_count,
                                                                            self.meta_data,
                                                                            self.children)
        else:
            return '*{}-{}, parent: {}, children: {}, meta_data: {}*'.format(self.child_count, self.meta_data_count,
                                                                             self.parent.child_count, self.meta_data,
                                                                             self.children)


def parse_nodes(numbers, parent):
    amount_of_child_nodes = numbers.pop(0)
    amount_of_meta_data_nodes = numbers.pop(0)

    node = Node(amount_of_child_nodes, amount_of_meta_data_nodes)
    node.parent = parent

    for node_index in range(0, amount_of_child_nodes):
        node.children.append(parse_nodes(numbers, node))

    for meta_data_index in range(0, amount_of_meta_data_nodes):
        node.meta_data.append(numbers.pop(0))

    return node


def calculate_sum(node):
    assert(node.child_count == len(node.children))

    value = 0

    if node.child_count == 0:
        for m in node.meta_data:
            value += m
    else:
        for md in node.meta_data:
            if md <= len(node.children) and md != 0:
                value += calculate_sum(node.children[md - 1])

    return value


root_node = parse_nodes(lines_8, None)

my_solution = calculate_sum(root_node)

print('{}, execution time: {:.2f} seconds'.format(my_solution, time.time() - start))

submit(my_solution, level=2, day=8, year=2018)
