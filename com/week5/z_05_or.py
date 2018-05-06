import numpy as np

def OR(x1, x2):
    x = np.array([x1, x2])
    weight = np.array([0.5, 0.5])
    theta = -0.2
    tmp = np.sum(x * weight) + theta

    if tmp <= 0:
        return 0
    else:
        return 1

if __name__ == '__main__':
    for xs in [(0, 0), (1, 0), (0, 1), (1, 1)]:
        print(xs[0], xs[1], "=>", OR(xs[0], xs[1]))
