import time
import numpy as np
from aocd import get_data

start = time.time()

lines_3 = get_data(day=3).split('\n')


class AdventPoint(object):
    def __init__(self, myx, myy):
        self.myx = myx
        self.myy = myy

    def __eq__(self, other):

        if isinstance(other, self.__class__):
            return self.myx == other.myx and self.myy == other.myy
        return False

    def __repr__(self):
        return 'x: {}, y: {}'.format(self.myx, self.myy)

    def __hash__(self):
        return hash(self.myx) ^ hash(self.myy)


class AdventRect(object):
    def __init__(self, p1, p2):
        self.left = min(p1.myx, p2.myx)
        self.right = max(p1.myx, p2.myx)
        self.bottom = max(p1.myy, p2.myy)
        self.top = min(p1.myy, p2.myy)
        self.width = self.right - self.left
        self.height = self.bottom - self.top

    def __repr__(self):
        return 'x: {}, y: {}, maxX: {}, maxY: {}'.format(self.left, self.top, self.right, self.bottom)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.left == other.left and self.right == other.right and self.bottom == other.bottom and self.top == other.top
        return False

    def contains_point(self, p1):
        return self.left <= p1.myx < self.right and self.top <= p1.myy < self.bottom


np.set_printoptions(threshold=np.nan)

rectangles = []

for line in lines_3:
    top_left = line.split()[2].replace(':', '').split(',')
    width_height = line.split()[3].split('x')
    x = int(top_left[0])
    y = int(top_left[1])
    width = int(width_height[0])
    height = int(width_height[1])
    rectangle = AdventRect(AdventPoint(x, y), AdventPoint(x + width, y + height))
    rectangles.append(rectangle)


min_x = 999999
min_y = 999999
max_x = 0
max_y = 0

for rectangle in rectangles:
    min_x = min(min_x, rectangle.left)
    min_y = min(min_y, rectangle.top)
    max_x = max(max_x, rectangle.right + 1)
    max_y = max(max_y, rectangle.bottom + 1)

fabric = np.zeros((max_x, max_y))

for rectangle in rectangles:
    fabric.T[rectangle.top:rectangle.bottom, rectangle.left:rectangle.right] += 1

one_dim = fabric.reshape(1, -1)[0]
greater_one = np.where(one_dim > 1)
print(len(greater_one[0]), 'execution time: {:.2f} seconds'.format(time.time() - start))
