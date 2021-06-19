import numpy as np

x=np.array([(23,24,25,26),(27,28,29,30),(31,32,33,34)])

print(x.sum(axis=0))
print(x.sum(axis=1))

print(np.sqrt(x))
print(np.square(x))
print(np.std(x))

