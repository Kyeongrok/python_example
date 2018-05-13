## Perceptron(퍼셉트론)이란?
여러개의 값을 받아서 가중치에 따라 결과를 알려주는 것

## AND
둘 다 true여야 true
```python
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

```

결과
```text
0 0 => 0
0 1 => 0
1 0 => 0
1 1 => 1
```


## OR
둘 중에 하나만 true라도 true


## NAND
둘 중에 하나라도 false면 true
```python
import numpy as np

def NAND(x1, x2):
    x = np.array([x1, x2])
    weight = np.array([-0.5, -0.5])
    theta = 0.7
    tmp = np.sum(x * weight) + theta

    if tmp <= 0:
        return 0
    else:
        return 1

if __name__ == '__main__':
    for xs in [(0, 0), (0, 1), (1, 0), (1, 1)]:
        print(xs[0], xs[1], "=>", NAND(xs[0], xs[1]))
```

결과
```text
0 0 => 1
0 1 => 1
1 0 => 1
1 1 => 0
```

## XOR
두개가 다를 때만 true

```python
print("----xor----")
# 연결은 어떻게 해야 하는가?
for item in [(0, 0), (0, 1), (1, 0), (1, 1)]:
    print(AND(OR(item[0], item[1]), NAND(item[0], item[1])))
```

결과
```text
0 0 => 0
0 1 => 1
1 0 => 1
1 1 => 0
```
