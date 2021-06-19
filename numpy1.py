import time

import numpy as np
import sys

'''
a = np.array([1, 2, 3])
b = np.array([(1, 2, 3), (-4, -5, -6), (0.7, 0.8, 0.9), (-0.01, -0.011, -0.012)])

print(a)
print(b)
'''

# comparing size of list and numpy array
'''
c = range(1000)
print(sys.getsizeof(500) * len(c))

d = np.arange(1000)
print(d.size*d.itemsize)
'''

# comparing time taken to compute sum of two lists and sum of two numpy arrays
SIZE = 1000000

l1 = range(SIZE)
l2 = range(SIZE)

p1 = np.arange(SIZE)
p2 = np.arange(SIZE)

start = time.time()

result = [(x, y) for x, y in zip(l1, l2)]

print((time.time()-start)*1000)

start = time.time()

result = p1+p2

print((time.time()-start)*1000)

