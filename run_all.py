import os 
import time
from collections import deque


start = time.time()

# for day in range(1, 10):
#     day_string = 'day_{:02d}'.format(day)
#     print(day_string)
#     os.system('python3 {}_part_1.py'.format(day_string))
#     os.system('python3 {}_part_2.py'.format(day_string))
#
# print('********* FULL TIME FOR ALL {:.2f} seconds'.format(time.time() - start))


testing = deque([1, 2, 3, 4, 5])
print(testing)
print(testing.rotate(1))
print(testing)
testing.append(6)
print(testing)
