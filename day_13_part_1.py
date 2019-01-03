import time
from aocd import get_data
from aocd import submit
import itertools
from enum import Enum
import operator

lines_13 = get_data(day=13).split('\n')
# lines_13 = ['/->-\\', '|   |  /----\\', '| /-+--+-\  |', '| | |  | v  |', '\-+-/  \-+--/', '  \------/']


class Direction(Enum):
    UP = 1
    RIGHT = 2
    DOWN = 3
    LEFT = 4

    def turn_left(self):
        if self == Direction.UP:
            return Direction.LEFT
        elif self == Direction.LEFT:
            return Direction.DOWN
        elif self == Direction.DOWN:
            return Direction.RIGHT
        elif self == Direction.RIGHT:
            return Direction.UP

    def turn_right(self):
        if self == Direction.UP:
            return Direction.RIGHT
        elif self == Direction.LEFT:
            return Direction.UP
        elif self == Direction.DOWN:
            return Direction.LEFT
        elif self == Direction.RIGHT:
            return Direction.DOWN


class Track:
    def __init__(self, track, x, y):
        self.track = track
        self.x = x
        self.y = y
        self.vehicles = []
        self.upper = None
        self.lower = None
        self.left = None
        self.right = None


class Vehicle:
    def __init__(self, initial_direction, track):
        self.current_direction = initial_direction
        self.track = track
        self.next_intersection_direction = 'l'

    def drive_forward(self):
        next_direction: Direction

        if self.track.track == '\\':
            if self.current_direction == Direction.RIGHT:
                next_direction = Direction.DOWN
            elif self.current_direction == Direction.UP:
                next_direction = Direction.LEFT
            elif self.current_direction == Direction.LEFT:
                next_direction = Direction.UP
            elif self.current_direction == Direction.DOWN:
                next_direction = Direction.RIGHT
        elif self.track.track == '/':
            if self.current_direction == Direction.UP:
                next_direction = Direction.RIGHT
            elif self.current_direction == Direction.LEFT:
                next_direction = Direction.DOWN
            elif self.current_direction == Direction.RIGHT:
                next_direction = Direction.UP
            elif self.current_direction == Direction.DOWN:
                next_direction = Direction.LEFT
        elif self.track.track == '+':
            if self.next_intersection_direction == 'l':
                next_direction = self.current_direction.turn_left()
                self.next_intersection_direction = 's'
            elif self.next_intersection_direction == 's':
                next_direction = self.current_direction
                self.next_intersection_direction = 'r'
            else:
                next_direction = self.current_direction.turn_right()
                self.next_intersection_direction = 'l'
        elif self.current_direction == Direction.RIGHT:
            next_direction = Direction.RIGHT
        elif self.current_direction == Direction.UP:
            next_direction = Direction.UP
        elif self.current_direction == Direction.LEFT:
            next_direction = Direction.LEFT
        elif self.current_direction == Direction.DOWN:
            next_direction = Direction.DOWN

        self.current_direction = next_direction

        if next_direction == Direction.LEFT:
            self.track.left.vehicles.append(self)
            self.track.vehicles.remove(self)
            self.track = self.track.left
        elif next_direction == Direction.UP:
            self.track.upper.vehicles.append(self)
            self.track.vehicles.remove(self)
            self.track = self.track.upper
        elif next_direction == Direction.DOWN:
            self.track.lower.vehicles.append(self)
            self.track.vehicles.remove(self)
            self.track = self.track.lower
        elif next_direction == Direction.RIGHT:
            self.track.right.vehicles.append(self)
            self.track.vehicles.remove(self)
            self.track = self.track.right

        if len(self.track.vehicles) > 1:
            return '{},{}'.format(self.track.x, self.track.y)
        else:
            return None


start = time.time()

tracks = []
vehicles = []


def parse_input():
    for y, line in enumerate(lines_13):
        for x, character in enumerate(list(line)):
            if character == '>':
                track = Track('-', x, y)
                tracks.append(track)
                vehicle = Vehicle(Direction.RIGHT, track)
                track.vehicles.append(vehicle)
                vehicles.append(vehicle)
            elif character == '^':
                track = Track('|', x, y)
                tracks.append(track)
                vehicle = Vehicle(Direction.UP, track)
                track.vehicles.append(vehicle)
                vehicles.append(vehicle)
            elif character == 'v':
                track = Track('|', x, y)
                tracks.append(track)
                vehicle = Vehicle(Direction.DOWN, track)
                track.vehicles.append(vehicle)
                vehicles.append(vehicle)
            elif character == '<':
                track = Track('-', x, y)
                tracks.append(track)
                vehicle = Vehicle(Direction.LEFT, track)
                track.vehicles.append(vehicle)
                vehicles.append(vehicle)
            elif character == '|':
                tracks.append(Track('|', x, y))
            elif character == '-':
                tracks.append(Track('-', x, y))
            elif character == '/':
                tracks.append(Track('/', x, y))
            elif character == '\\':
                tracks.append(Track('\\', x, y))
            elif character == '+':
                tracks.append(Track('+', x, y))
            else:
                continue

    i = 0

    for track_combination in itertools.product(tracks, tracks):
        i += 1

        first_track = track_combination[0]
        second_track = track_combination[1]

        if first_track.x == second_track.x and abs(first_track.y - second_track.y) == 1:
            if first_track.y > second_track.y:
                first_track.upper = second_track
                second_track.lower = first_track
            else:
                first_track.lower = second_track
                second_track.upper = first_track
        elif first_track.y == second_track.y and abs(first_track.x - second_track.x) == 1:
            if first_track.x > second_track.x:
                first_track.left = second_track
                second_track.right = first_track
            else:
                first_track.right = second_track
                second_track.left = first_track


parse_input()

while True:
    vehicles.sort(key=operator.attrgetter('track.x', 'track.y'))

    for currently_driving_vehicle in vehicles:
        result = currently_driving_vehicle.drive_forward()

        if result is not None:
            print('{}, execution time: {:.2f} seconds'.format(result, time.time() - start))
            submit(result, level=1, day=13, year=2018)
            exit(0)
