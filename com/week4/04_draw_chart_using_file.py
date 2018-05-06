import numpy as np
import matplotlib.pylab as plt

f1 = open("./random_number.txt", mode='r')
lines = f1.readlines()

datas = []
for line in lines:
    datas.append(line.replace("\n", ""))

print(datas)

plt.plot(np.arange(1, len(datas)+1, 1), datas)
plt.show()