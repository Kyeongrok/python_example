import numpy as np
import matplotlib.pylab as plt

x = np.arange(1, 10 + 1, 0.1)
y = np.sin(x)

plt.plot(x, y)
plt.grid()
plt.show()

