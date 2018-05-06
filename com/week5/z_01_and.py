# and
'''
v1, v2가 둘다 true일 때 true
'''
import numpy as np

def AND(x1, x2):
    x = np.array([x1, x2])
    weight = np.array([0.5, 0.5])
    theta = -0.7
    tmp = np.sum(x * weight) + theta

    if tmp <= 0:
        return 0
    else:
        return 1

if __name__ == '__main__':
    for xs in [(0, 0), (0, 1), (1, 0), (1, 1)]:
        print(xs[0], xs[1], "=>", AND(xs[0], xs[1]))

