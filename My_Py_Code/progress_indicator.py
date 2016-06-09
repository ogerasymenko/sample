'''

Created on June 07, 2016.

'''

__author__ = 'sashko'

import sys
import time

for i in range(5, 101, 5):
    sys.stdout.write("\rThinking...{0}".format(i))
    sys.stdout.flush()
    time.sleep(0.2)
    
print('\nDone.')
