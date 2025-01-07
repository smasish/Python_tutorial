import numpy as np, pprint as pp, copy, matplotlib.pyplot as plt, matplotlib as mpl
# 2. Create special ndarrays
zero = np.zeros((3,4)) # a matrix of zeros
one = np.ones((4,3), dtype=np.int64) # a matrix of ones, specify data type
emty = np.empty((3,3)) # no really empty, just don't care what are inside the memory
unit = np.eye((3)) # unit matrix
cons = np.full((2,3), 2.8) # constant matrix
ran = np.random.random((2,2)) # random matrix
print(f'{zero=}\n{one=}\n{emty=}\n{unit=}\n{cons=}\n{ran=}')