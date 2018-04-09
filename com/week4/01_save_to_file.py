import numpy as np

result = np.arange(10)

f1 = open("./a.txt", mode='w+')
f1.write("hello\n")
f1.write("nello\n")
f1.close()



numbers = np.random.randint(1, 2000, 1000, dtype='i')
f2 = open("./c.txt", mode='w+')
for number in numbers:
    f2.write(str(number) + "\n")
f2.close()

