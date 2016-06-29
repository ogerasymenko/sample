__author__ = 'sashko'

from functools import lru_cache
from timeit import Timer


@lru_cache(maxsize=None)
def fibs(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fibs(n-1) + fibs(n-2)

print(fibs(35))


code2 = """\
def fibonacci(n):
  if n == 0 or n == 1:
    return 1
  else:
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(35))
"""
t2 = Timer(stmt=code2)
print('Second value calculated during:', round(t2.timeit(number=1), 2), 'seconds')
