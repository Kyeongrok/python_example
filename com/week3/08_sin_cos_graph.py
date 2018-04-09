import numpy as np
import matplotlib.pylab as plt

x = np.arange(1, 10 + 1, 0.1)
y = np.sin(x)
z = np.cos(x)

print(x)
print(y)

plt.grid()
plt.plot(x, y)
plt.draw()
plt.plot(x, z)
plt.draw()

