import numpy as np

# array만드는 법 np로
x = np.array([1, 2, 3])
# []대괄호는 array(배열)다.

y = np.array([1, 2, 3], dtype=float)

print(type(x))
print(type(x[0]))

print(x)
print(y)
print(y[0], type(y[0]))
print(y[1], type(y[1]))
print(y[2], type(y[2]))


