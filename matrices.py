import numpy as np

# We can also use array to create matrices that can represent operations.
M1 = np.array([[1, 1], [0, 0]]) # const 0 
M2 = np.array([[1, 0], [0, 1]]) # identity
M = (M1 + M2)/2
print(M)
# output:
# [[1.  0.5]
#  [0.  0.5]]