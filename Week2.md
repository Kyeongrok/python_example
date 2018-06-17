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

## Array(어레이)란?
[] 대괄호로 시작해서 대괄호로 끝나는 것
안에 여러가지 숫자나 문자열 오브젝트 등을 0개 또는 그 이상 넣을 수 있습니다.
```python
numbers = [1, 2, 3]
users = ["kyeongrok", "jihyun"]
range1 = list(range(0, 10)) # 얘도 어레이
```

list(리스트)의 성질을 가집니다. 어떤거냐면 추가 삭제를 할 수 있는 것입니다.

## range(0, 10)이란?
```python
print(range(0, 10))
# 결과
# range(0, 10)
```
range(0, 10)에 뭐가 들어있는지 보려면 list()로 감싸서 출력을 해야 합니다. list()는 받은 데이터를 []형태로 만들어 주는 함수 입니다. 
```python
print(list(range(0, 10)))
````

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

### 2~9단 출력하기
구구단을 출력하는 코드를 함수 안으로 넣고 반복문을 이용해 여러번 호출을 할 수 있습니다.
```python
def print_gugudan(dan):
    for item in range(1, 10):
        print(dan, "*", item, "=", dan *item)

for dan in range(2, 10):
    print_gugudan(dan)

```

결과
```text
2 * 1 = 2
2 * 2 = 4
2 * 3 = 6
2 * 4 = 8
2 * 5 = 10
2 * 6 = 12
---- 중략 ----
9 * 7 = 63
9 * 8 = 72
9 * 9 = 81
```
