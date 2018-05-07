## 반복문(for문)
반복문은 내가 지정한 숫자의 범위만큼 반복을 하는 명령 입니다.
```python
for item in range(0, 10):
    print(item)
```

* for로 시작을 합니다. 한칸을 띄웁니다.
```python
for 
```
* item이라고 변수 이름을 씁니다. 한칸을 띄웁니다.
```python
for item 
```
* in을 씁니다. 한칸을 띄웁니다. 뒤에 있는것 안에서 뽑아온다는 뜻입니다.
```python
for item in 
```
* range(0, 10)이라고 씁니다. 0 ~ 9까지 숫자 목록(list)을 만들어줍니다.
```python
for item in range(0, 10)
```
* :를 붙입니다.
```python
for item in range(0, 10):
```
* 엔터를 칩니다.
* tab으로 들여쓰기를 합니다.
* print(item)을 입력합니다. item에 0부터 9까지 10개의 숫자가 들어옵니다.
```python
for item in range(0, 10):
    print(item)
```
결과
```text
0
1
2
3
4
5
6
7
8
9
```

### 0~10이 나오게 하려면?
```python
for item in range(0, 11):
    print(item)
```
결과
```text
0
1
2
3
4
5
6
7
8
9
10
```

## range(0, 10)이란?
```python
print(range(0, 10))
# 결과
# range(0, 10)
```
range(0, 10)에 뭐가 들어있는지 보려면 list()로 감싸서 출력을 해야 합니다. list()는 받은 데이터를 []형태로 만들어 주는 함수 입니다. 
```python
print(list(range(0, 10)))
```

이렇게도 출력을 할 수 있습니다.
```python
print([0, 1, 2, 2])
```


## 구구단 2단 출력하기
구구단은 반복문과 print()를 연습하기 좋은 예제 입니다.
반복문을 이용해 구구단을 출력 해봅시다.

* 여러개의 값들 한줄에 출력하기
```python
print(2, 1, 2)
print(2, "*", 1, "=", 2)
```

* 2 1, 2 2 처럼 앞에 2붙이기
```python
for item in range(1, 10):
    print(2, item)
```

* 숫자들 사이에 기호 넣기
```python
for item in range(1, 10):
    print(2, "*", item, "=", 2 *item)
```

