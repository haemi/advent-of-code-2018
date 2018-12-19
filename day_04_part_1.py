from typing import List, Tuple

import numpy as np
import operator
import time
from aocd import get_data

start = time.time()

lines_4 = get_data(day=4).split('\n')

guards = {}

current_guard_id = 0
current_asleep_time = 0

for line in sorted(lines_4):
    date_time = line[0:18]
    state_string = line[19:].replace('\n', '')

    if 'Guard #' in state_string:
        current_guard_id = int(state_string.replace('Guard #', '').replace(' begins shift', ''))
    elif 'wakes' in state_string:
        woke_up = int(date_time[-3:-1])

        if current_guard_id not in guards:
            guards[current_guard_id] = np.zeros(60)
        guards[current_guard_id][current_asleep_time:woke_up] += 1
    elif 'asleep' in state_string:
        current_asleep_time = int(date_time[-3:-1])

sleep_minutes = {}

for guard in guards:
    sleep_minutes[guard] = np.sum(guards[guard])

sorted_guards: List[Tuple[int, int]] = sorted(sleep_minutes.items(), key=operator.itemgetter(1), reverse=True)
sleepy_guard = sorted_guards[0][0]

max_sleep_minute = np.argmax(guards[sleepy_guard])

print(sleepy_guard * max_sleep_minute, 'execution time: {:.2f} seconds'.format(time.time() - start))
