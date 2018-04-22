import numpy as np

numbers = np.random.randint(1, 2000, 1000, dtype='i')
f2 = open("./c.txt", mode='w+')
for number in numbers:
    f2.write(str(number) + "\n")
f2.close()
