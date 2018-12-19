import time
from aocd import get_data

start = time.time()

lines_7 = get_data(day=7).split('\n')


class Production(object):
    def __init__(self, l):
        super(Production, self).__init__()
        self.letter = l
        self.vorgaenger = []

    def __eq__(self, other):
        return self.letter == other.letter

    def __repr__(self):
        return '{}, vorgaenger: {}'.format(self.letter, list(map(lambda x: x.letter, self.vorgaenger)))


letters = []


for line in lines_7:
    first_character = line.replace('\n', '')[5:6]
    second_character = line.replace('\n', '')[36:37]

    if first_character not in map(lambda x: x.letter, letters):
        first_letter = Production(first_character)
        letters.append(first_letter)
    else:
        for temp_letter in letters:
            if temp_letter.letter == first_character:
                first_letter = temp_letter
                break

    if second_character not in map(lambda x: x.letter, letters):
        second_letter = Production(second_character)
        letters.append(second_letter)
    else:
        for temp_letter in letters:
            if temp_letter.letter == second_character:
                second_letter = temp_letter
                break

    # noinspection PyUnboundLocalVariable
    second_letter.vorgaenger.append(first_letter)

solution = []

while len(letters) > 0:
    no_vorgaenger = list(filter(lambda x: len(x.vorgaenger) == 0, letters))

    newly_insert = sorted(no_vorgaenger, key=lambda x: x.letter)[0]
    current_index = len(solution) - 1

    solution.append(newly_insert)

    for letter in list(letters):
        if letter.letter == newly_insert.letter:
            letters.remove(letter)
        else:
            if newly_insert in letter.vorgaenger:
                letter.vorgaenger.remove(newly_insert)


solution_letters = map(lambda x: x.letter, solution)
print(''.join(solution_letters), 'execution time: {:.2f} seconds'.format(time.time() - start))
