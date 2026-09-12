import numpy as np

ket0 = np.array([[1], [0]])
ket1 = np.array([[0], [1]])

M1 = np.array([[1, 1], [0, 0]])
M2 = np.array([[1, 0], [0, 1]])

M = (M1+M2)/2

# @ is a operator for matrix multiplication
print(M1 @ ket1)
print(M1 @ M2)
print(M @ M)

# output: 
# 
# [[1]
#  [0]]
# 
# [[1 1]
#  [0 0]]
# [[1.   0.75]
#  [0.   0.25]]
