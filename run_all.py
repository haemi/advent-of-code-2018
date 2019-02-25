import os 
import time


start = time.time()

for day in range(1, 15):
    day_string = 'day_{:02d}'.format(day)
    print(day_string)
    os.system('python3 {}_part_1.py'.format(day_string))
    os.system('python3 {}_part_2.py'.format(day_string))

print('********* FULL TIME FOR ALL {:.2f} seconds'.format(time.time() - start))
