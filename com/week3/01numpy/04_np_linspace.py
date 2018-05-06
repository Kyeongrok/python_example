import numpy as np

x = np.linspace(1, 10, 10)

print(x)

# ex) 10000 ~ 99999까지 숫자 700개 정수
nums = np.linspace(10000, 99999, 700, dtype=int)
print(nums)
print(len(nums))
