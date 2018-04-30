import numpy as np

# 1, 10, 10개
# 2.0부터 3.0까지 5개를 만들면 간격은 같을까?
x = np.linspace(2.0, 3.0, num=4, dtype=int)
print(x)
print(type(x[0]))