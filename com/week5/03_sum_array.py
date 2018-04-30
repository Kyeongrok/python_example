import numpy as np
x = np.array([1, 2])
weight = np.array([0.5, 0.5])

xweight = x * weight

print(np.sum(xweight))
