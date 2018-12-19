import time
from aocd import get_data
from string import ascii_lowercase

start = time.time()

lines_2 = get_data(day=2).split('\n')

zweier = 0
dreier = 0

for word in lines_2:
    found_zweier = False
    found_dreier = False

    for character in ascii_lowercase:
        if word.count(character) == 2 and not found_zweier:
            found_zweier = True
            zweier += 1
        elif word.count(character) == 3 and not found_dreier:
            found_dreier = True
            dreier += 1

print(zweier * dreier, 'execution time: {:.2f} seconds'.format(time.time() - start))
