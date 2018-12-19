import stringdist
import difflib
import time
from aocd import get_data
import itertools

start = time.time()

lines_2 = get_data(day=2).split('\n')

for word1, word2 in itertools.product(lines_2, lines_2):
    if stringdist.levenshtein(word1, word2) == 1:
        matches = difflib.SequenceMatcher(None, word1, word2).get_matching_blocks()
        code = ''
        for match in matches:
            code += word1[match.a:match.a + match.size]
        print(code.replace('\n', ''), 'execution time: {:.2f} seconds'.format(time.time() - start))
        break
