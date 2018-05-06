import numpy as np

file_name = "./random_number.txt"
numbers = np.random.randint(1, 2000, 1000, dtype='i')
f2 = open(file_name, mode='w+')
for number in numbers:
    f2.write(str(number) + "\n")
f2.close()
