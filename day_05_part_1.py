import time
from aocd import get_data

start = time.time()

lines_5 = get_data(day=5)


def remove_at(i, s):
    return s[:i] + s[i+2:]


def find_final_polymer(inputstring):
    idx = 0

    while idx < len(inputstring) - 1:
        current_character = inputstring[idx]
        next_character = inputstring[idx + 1]

        if next_character.lower() == current_character.lower() and next_character != current_character:
            inputstring = remove_at(idx, inputstring)
            idx = max(0, idx - 1)
        else:
            idx += 1

    return inputstring


print(len(find_final_polymer(lines_5)), 'execution time: {:.2f} seconds'.format(time.time() - start))
