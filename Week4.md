## 파이썬으로 차트 그리기

### matplot.pylab 임포트 하기
```python
import numpy as np
import matplotlib.pylab as plt
```

### y = x 그래프 그리기
```python
import matplotlib.pylab as plt
```

# y = x
```python
import matplotlib.pylab as plt

# y = x
x = [1, 2, 3]
y = [1, 2, 3]

plt.plot(x, y)
plt.show()
```

### y = 2x 그래프 그리기
```python
import matplotlib.pylab as plt

# y = 2x
x = [1, 2, 3]
y = [2, 4, 6]

plt.plot(x, y)
plt.show()
```

### y = 2x + 1 그래프 그리기
```python
import matplotlib.pylab as plt
import numpy as np

# y = 2x
# y = 2x + 1
x = np.arange(1, 10, 1)
y = 2 * x + 1

plt.plot(x, y)
plt.show()

```

### sin그래프 그리기
```python
import numpy as np
import matplotlib.pylab as plt

x = np.arange(1, 10 + 1, 0.1)
y = np.sin(x)

plt.plot(x, y)
plt.grid()
plt.show()

```

### sin, cos그래프 동시에 그리기
```python
import numpy as np
import matplotlib.pylab as plt

x = np.arange(1, 10 + 1, 0.1)
y = np.sin(x)
z = np.cos(x)

print(x)
print(y)

plt.grid()
plt.plot(x, y)
plt.draw()
plt.plot(x, z)
plt.draw()

plt.show()

```



### 파일에 저장하기
hello.txt라는 파일을 만들고 첫번째 줄에 hello, 두번째 줄에 nello를 넣는 예제 입니다. 
```python
f1 = open("./hello.txt", mode='w+')
f1.write("hello\n")
f1.write("nello\n")
f1.close()
print("파일 저장이 완료 되었습니다. 같은 폴더에 hello.txt를 찾아보세요.")
```
위 코드를 실행 하면 같은 위치에 hello.txt파일이 만들어 집니다. 이미 hello.txt가 있다면 덮어쓰기가 됩니다.

파일을 열어보면 아래와 같이 hello, nello가 들어 있습니다.
```text
hello
nello
```

### 1 to 10까지 저장하기
```python
f1 = open("./1_to_10.txt", mode='w+')
f1.write("1\n")
f1.write("2\n")
f1.write("3\n")
f1.write("4\n")
f1.write("5\n")
f1.write("6\n")
f1.write("6\n")
f1.write("7\n")
f1.write("8\n")
f1.write("9\n")
f1.write("10\n")
f1.close()
print("파일 저장이 완료 되었습니다. 같은 폴더에 1_to_10.txt를 찾아보세요.")
```

### 1 to 100 저장하기
```python
file_name = "./1_to_100.txt"
f1 = open(file_name, mode='w+')
for number in range(1, 101):
    f1.write(str(number) + "\n")
f1.close()
print("파일 저장이 완료 되었습니다. 같은 폴더에 {}를 찾아보세요.".format(file_name))
```

### 파일에서 불러오기
hello.txt파일을 불러와서 안에 있는 내용을 콘솔에 출력 하는 예제 입니다. 
```python
f1 = open("./hello.txt", mode='r')
lines = f1.readlines()

datas = []
for line in lines:
    datas.append(line.replace("\n", ""))

print(datas)
```
