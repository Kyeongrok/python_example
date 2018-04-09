import matplotlib.pylab as plt
import numpy as np

f1 = open("./c.txt", mode='r')
lines = f1.readlines()

datas = []
for line in lines:
    datas.append(line.replace("\n", ""))

x = np.arange(1, 1001, 1)
y = np.array(datas)


print(len(x))
print(len(y))
plt.plot(x, y)
plt.show()
