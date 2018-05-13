import numpy as np
from com.week5.z_01_and import AND
from com.week5.z_04_nand import NAND
from com.week5.z_05_or import OR

print("---or----")
for item in [(0, 0), (0, 1), (1, 0), (1, 1)]:
    print(OR(item[0], item[1]))

print("---nand----")

for item in [(0, 0), (0, 1), (1, 0), (1, 1)]:
    print(NAND(item[0], item[1]))

print("----xor----")
# 연결은 어떻게 해야 하는가?
for item in [(0, 0), (0, 1), (1, 0), (1, 1)]:
    print(AND(OR(item[0], item[1]), NAND(item[0], item[1])))
