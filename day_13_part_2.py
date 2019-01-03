import time
from aocd import get_data
from aocd import submit
from enum import Enum
import operator

lines_13 = get_data(day=13).split('\n')
# lines_13 = ['/>-<\  ', '|   |  ', '| /<+-\\', '| | | v', '\\>+</ |', '  |   ^', '  \<->/']


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

    def not_crashed_vehicles(self):
        return list(filter(lambda x: not x.crashed, self.vehicles))


class Vehicle:
    def __init__(self, initial_direction, track):
        self.current_direction = initial_direction
        self.track = track
        self.next_intersection_direction = 'l'
        self.crashed = False

    def drive_forward(self, tick_number):
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
            elif self.next_intersection_direction == 'r':
                next_direction = self.current_direction.turn_right()
                self.next_intersection_direction = 'l'
            else:
                exit(1)
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

        if len(self.track.not_crashed_vehicles()) > 1:
            print('{} crashed into {} at {},{} on tick {}'.format(self.track.not_crashed_vehicles()[0].current_direction, self.track.not_crashed_vehicles()[1].current_direction, self.track.x, self.track.y, tick_number))
            for v in self.track.vehicles:
                v.crashed = True
                self.track.vehicles = []
            return None
        elif len(list(filter(lambda x: not x.crashed, vehicles))) == 1:
            return '{},{}'.format(list(filter(lambda x: not x.crashed, vehicles))[0].track.x, list(filter(lambda x: not x.crashed, vehicles))[0].track.y)
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
                track = Track('|', x, y)
                tracks.append(track)
            elif character == '-':
                track = Track('-', x, y)
                tracks.append(track)
            elif character == '/':
                track = Track('/', x, y)
                tracks.append(track)
            elif character == '\\':
                track = Track('\\', x, y)
                tracks.append(track)
            elif character == '+':
                track = Track('+', x, y)
                tracks.append(track)
            else:
                continue

            link_track(track)


def link_track(track):
    if track is not None:
        for second_track in tracks:
            if second_track == track:
                continue
            if track.x == second_track.x and abs(track.y - second_track.y) == 1:
                if track.y > second_track.y:
                    track.upper = second_track
                    second_track.lower = track
                else:
                    track.lower = second_track
                    second_track.upper = track
            elif track.y == second_track.y and abs(track.x - second_track.x) == 1:
                if track.x > second_track.x:
                    track.left = second_track
                    second_track.right = track
                else:
                    track.right = second_track
                    second_track.left = track


parse_input()

i = 1

while True:
    vehicles.sort(key=operator.attrgetter('track.y', 'track.x'))

    for currently_driving_vehicle in filter(lambda x: not x.crashed, vehicles):
        result = currently_driving_vehicle.drive_forward(i)

        if result is not None:
            print('{}, execution time: {:.2f} seconds'.format(result, time.time() - start))
            submit(result, level=2, day=13, year=2018)
            exit(0)

    vehicles = list(filter(lambda x: not x.crashed, vehicles))

    i += 1
