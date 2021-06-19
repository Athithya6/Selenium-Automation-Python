import numpy as np

a = np.array([1, 2, 3])
b = np.array([(-4, -5, -6, -7), (-9, -10, -11, -12)])
c = np.array([(-12, 13, -14), (15, -16, 17), (-18, 19, -20), (21, -22, 23)])
d = np.array([0.1, -0.2, 0.3, -0.4])
e = np.array([(0.1, 998, -456, -689.045, -33445, 0.1117778), (-8.7766, 12678, -333, 190.876, -76, 0.112)])

print(b)
print(b.reshape(4, 2))
print(b.reshape(8, 1))
print(b.reshape(1, 8))

print(e)
print(e.reshape(1, 12))
print(e.reshape(3, 4))
