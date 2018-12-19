import time
from aocd import get_data
from aocd import submit

start = time.time()

lines_7 = get_data(day=7).split('\n')


class Production(object):
    def __init__(self, l):
        super(Production, self).__init__()
        self.letter = l
        self.vorgaenger = []
        self.amount_of_time = ord(l) - 4
        self.currently_in_work = False

    def __eq__(self, other):
        return self.letter == other.letter

    def __repr__(self):
        return 'vorgaenger: {}, {}, time left: {}, in_progress: {}'.format(list(map(lambda x: x.letter, self.vorgaenger)), self.letter, self.amount_of_time, self.currently_in_work)


letters = []
number_of_workers = 5

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

seconds = -1

while len(letters) > 0:
    no_vorgaenger = list(filter(lambda x: len(x.vorgaenger) == 0, letters))

    in_progress = sorted(no_vorgaenger, key=lambda x: (not x.currently_in_work, x.letter))[0:min(number_of_workers, len(no_vorgaenger))]
    current_index = len(solution) - 1

    seconds += 1

    for p in in_progress:
        p.currently_in_work = True
        p.amount_of_time -= 1

    in_progress = list(filter(lambda x: x.amount_of_time == 0, in_progress))

    for letter in list(letters):
        if letter in in_progress:
            solution.append(letter)
            letters.remove(letter)
        else:
            for ni in in_progress:
                if ni in letter.vorgaenger:
                    letter.vorgaenger.remove(ni)

print('seconds: {}'.format(seconds + 1), 'execution time: {:.2f} seconds'.format(time.time() - start))
submit(seconds + 1, level=2, day=7, year=2018)
