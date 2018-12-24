import time
from aocd import get_data
from aocd import submit
import regex as re

lines_12 = get_data(day=12).split('\n')

start = time.time()

initial_state = lines_12[0].replace('initial state: ', '')
number_of_generations = 20
offset = 0
rules = lines_12[2:]
rules = list(filter(lambda x: x.endswith('#'), rules))
current_generation_string = initial_state

for generation in range(1, number_of_generations + 1):
    if current_generation_string.find('#') < 5:
        current_generation_string = '.....{}'.format(current_generation_string)
        offset += 5

    if current_generation_string.rfind('#') > len(current_generation_string) - 5:
        current_generation_string = '{}.....'.format(current_generation_string)

    next_generation_string = list(current_generation_string.replace('#', '.'))

    for rule in rules:
        rule_to_use = rule.replace(' => #', '').replace('.', '\\.')

        indices = [m.start() for m in re.finditer(rule_to_use, current_generation_string, overlapped=True)]
        for index in indices:
            next_generation_string[index + 2] = '#'

    current_generation_string = ''.join(next_generation_string)
    next_generation_string = list(current_generation_string.replace('#', '.'))

my_solution = 0
for index in re.finditer('#', current_generation_string):
    my_solution += index.start() - offset

print('{}, execution time: {:.2f} seconds'.format(my_solution, time.time() - start))
submit(my_solution, level=1, day=12, year=2018)
