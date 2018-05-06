import matplotlib.pylab as plt
import numpy as np

# y = 2x
# y = 2x + 1
x = np.arange(1, 10, 1)
y = 2 * x + 1

plt.plot(x, y)
plt.show()
