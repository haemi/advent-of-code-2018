import time
from aocd import get_data
from aocd import submit
import regex as re

lines_12 = get_data(day=12).split('\n')

start = time.time()

initial_state = lines_12[0].replace('initial state: ', '')
number_of_generations = 50000000000
offset = 0
rules = lines_12[2:]
rules = list(filter(lambda x: x.endswith('#'), rules))
current_generation_string = initial_state

previous_state = initial_state

for generation in range(1, number_of_generations + 1):
    offset -= current_generation_string.index('#')

    current_generation_string = current_generation_string.lstrip('.')
    current_generation_string = current_generation_string.rstrip('.')
    current_generation_string = '.....{}.....'.format(current_generation_string)

    offset += 5

    next_generation_string = list(current_generation_string.replace('#', '.'))

    for rule in rules:
        rule_to_use = rule.replace(' => #', '').replace('.', '\\.')

        indices = [m.start() for m in re.finditer(rule_to_use, current_generation_string, overlapped=True)]
        for index in indices:
            next_generation_string[index + 2] = '#'

    current_generation_string = ''.join(next_generation_string)

    if previous_state == current_generation_string:
        offset += (number_of_generations - generation) * (5 - current_generation_string.index('#'))
        break

    previous_state = current_generation_string

my_solution = 0
for index in re.finditer('#', current_generation_string):
    my_solution += index.start() - offset

print('{}, execution time: {:.2f} seconds'.format(my_solution, time.time() - start))
submit(my_solution, level=2, day=12, year=2018)
