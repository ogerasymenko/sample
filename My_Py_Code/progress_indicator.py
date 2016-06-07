__author__ = 'sashko'

import sys, time

for i in range(5, 101, 5):
    sys.stdout.write("\rThinking...%s%%" % i)
    sys.stdout.flush()
    time.sleep(0.2)
print('\nDone.')
