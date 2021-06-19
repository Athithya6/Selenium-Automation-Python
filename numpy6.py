import numpy as np

x=np.array([(12,13,14,15,16),(-17,-18,-19,-20,-21)])
y=np.array([(12,13,14,15,16),(-17,-18,-19,-20,-21)])

#fundamental operations on arrays
print(x+y)
print(x-y)
print(x*y)
print(x/y)

#horizontal and vertical stacking of two arrays-one upon another
print(np.vstack((x,y)))
print(np.hstack((x,y)))

#printing an array as a single row
print(x.ravel())