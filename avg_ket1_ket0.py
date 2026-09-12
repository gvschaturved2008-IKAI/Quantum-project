import numpy as np

ket0 = np.array([[1],[0]]) #|0>
ket1 = np.array([[0],[1]]) #|1>

print((ket1 + ket0)/2) # avg of ket 0 and ket 1
# Output:
# [[0.5]
#  [0.5]]