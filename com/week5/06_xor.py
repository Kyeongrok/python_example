import numpy as np
from com.week5.z_01_and import AND
from com.week5.z_04_nand import NAND
from com.week5.z_05_or import OR

for item in [(0, 0), (0, 1), (1, 0), (1, 1)]:
    print(OR(item[0], item[1]))

print("-----------")

for item in [(0, 0), (0, 1), (1, 0), (1, 1)]:
    print(NAND(item[0], item[1]))


