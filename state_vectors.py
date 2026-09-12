# TheStatevector class in Qiskit provides functionality for defining and manipulating quantum state vectors. 
# In the code that follows, the Statevector class is imported and a few vectors are defined

from qiskit.quantum_info import Statevector
from numpy import sqrt

u = Statevector([1 / sqrt(2), 1 / sqrt(2)])
v = Statevector([(1 + 2.0j) / 3, -2 / 3])
w = Statevector([1 / 3, 2 / 3])

print(u.draw("text"))
print(u.draw("latex"))
print(u.draw("latex_source"))

# output:
# [0.70710678+0.j,0.70710678+0.j]
# <IPython.core.display.Latex object>(Bruhhhhhh...........)
# \frac{\sqrt{2}}{2} |0\rangle+\frac{\sqrt{2}}{2} |1\rangle

print(u.is_valid())
print(w.is_valid())

# output:
# True 
# False

print(v.draw("latex"))
# output:
# <IPython.core.display.Latex object>(sh*t)

outcome, state = v.measure()
print(f"Measured: {outcome}\nPost-measurement state:")
print(state.draw("latex"))

# output:
# Measured: 1
# Post-measurement state:
# -|1>
from qiskit.visualization import plot_histogram

statistics = v.sample_counts(1000)
plot_histogram(statistics)