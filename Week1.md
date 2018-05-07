## Programming이란
반복문에 function을 실행하는 것

## Interpreter 설정하기
Python3로 인터프린터가 설정 되어있는지 확인

File -> Settings -> interpreter 검색
    
## 프로젝트(project)
프로젝트란? 쉽게 말해 '폴더'라고 생각하시면 됩니다. 내가 만든 또는 필요한 파일들을 넣는 곳입니다.

### 프로젝트 만들기
    * Create Project를 누르세요
    * 경로설정을 해야합니다.

    * c:\git\python\python_practice_01

    * 우측 하단 Create
    * 그러면 파이썬이 빌드를 합니다.
    * 빌드가 완료되면 왼쪽에 project explorer가 나옵니다.
    * 왼쪽에 파일이 보이는 부분을 project explorer라고 합니다.

    * python_practice_01이라고 되어있는 부분이
    * project root(프로젝트 루트)입니다.

## package만들고 python파일 만들기
패키지란? 프로젝트 안에서 비슷한 파일들 끼리 저장해놓는 곳입니다.

    * 프로젝트 루트에서 오른쪽 버튼을 눌러서 context menu를 엽니다.
    * 마우스 오른쪽 버튼을 누르면 나오는 메뉴가 context메뉴 입니다.

    * New -> python package 선택합니다.

    * package이름을 com으로 합니다.
    * package는 폴더라고 생각하시면 됩니다.

    * 폴더(package)를 만들고 python파일을 만듭니다.
    

## 파이썬 파일 만들기
* 만든 package에서 context menu를 호출 합니다.
* new -> python file
* 파일명 01_hello

## hello 출력하기
```python
print("hello")
```
만든 파일에 위와 같이 입력 합니다.

## 실행 방법
    * 상단 메뉴run -> run
    * hello가 출력 되는 부분이 console 입니다.
결과
```text
hello
```

## function(함수)이란?
    * 펑션으로 읽는다. 함수로 번역 해놓았다.
    * f, fn, f(x)
    * python의 모든 기능들은 function으로 되어있다.
    * 값을 넣으면 특정 로직을 실행하고 때로는 결과값을 알려준다.
    * 함수는 선언을 하고 호출을 해야 실행된다.

## Function(함수)만들기
02_function.py를 만듭니다. Python File로 만듭니다.
```python
def print_hello():
    print("hello")
```

* def로 시작합니다.
* def는 함수를 선언하는 명령어 입니다.
```python
def
```
* def옆에 한칸을 띄웁니다.
```python
def 
```     
    
* 그 옆에는 이름(print_hello)을 적습니다.
```python
def print_hello
```
* 이름은 아무거나 가능합니다. ex)aaaa, bbb, plus, minus

* 이름 옆에는 ()를 붙인다.
```python
def print_hello()
```
* ()옆에는 :를 붙인다.
```python
def print_hello():
```    
* 엔터를 친다.
* tab을 넣는다
* 넣고 싶은 기능을 코딩한다. ex) print("hello")

```python
def print_hello():
    print("hello")
```

* 들여쓰기가 들어가지 않은 줄이 나올때까지를 function 으로 봅니다.


## function(함수) 실행하기, 호출하기
함수는 선언 한 후에 호출을 해주어야 실행이 되기 때문에 호출을 해줍니다.
```python
def print_hello():
    print("hello")
    
print_hello() #로 호출한다.
```
    * <함수 이름>()
    * <함수 이름>(파라메터)
    * <함수 이름>(파라메터1, 파라메터2)
    * mac 단축키 : ⌥ + ⌘ + R (10.5+)
    * window 단축키 : Ctrl + Shift + F10

## 변수와 상수
변수는 '변'하는 '수'(값)이고 상수는 항'상' 같은 '수'(값)

03_variable_constants.py
```python
result = 10
print(result)
result = 20
print(result)

print("10")
print("20")
```

* 변수는 값을 저장 하는 곳
* ex) hello = 10에서 앞에 hello
```python
hello = "world"
world = "hello"
```
* 상수는 "hello"와 같이 ""를 붙인다.
* 변수는 hello와 같이 ""를 안붙인다.

```python
hello = "world"
print(hello)
print("hello")
```
결과
```text
world
hello
```

https://github.com/Kyeongrok/python_example/blob/master/com/week1/04_parameter.py
## Parameter(파라메터)란?
함수를 호출 할 때 함수로 값을 넘겨줄 때 사용하는 변수. '파라메터'라고 읽습니다. 한글로 번역된 말은 '매개변수'입니다. p_message가 파라메터 입니다.
```python
def print_message(p_message):
    print(p_message)

print_message("bye")
```
* 함수 이름 옆에 ()안에 들어갑니다. ex) print_message(p_message)    
* 파라메터는 여러개를 만들 수 있습니다.

```python
def print_message(message):
    print(message)

print_message("bye")
```
위와 같이 p_message대신에 message라고 써도 됩니다. 파라메터의 이름이 중요한 것은 아닙니다.

## Parameter여러개 만들기
parameter를 이용하면 외부에서 여러개의 값을 받을 수 있다.
```python
def print_message_who(p_message, p_who):
    print(p_message, p_who)

print_message_who("hello", "kyeongrok")
```

## return이란?
리턴이라고 읽는다. 돌려준다 반환한다 등으로 번역되었다.
* 함수를 실행한 결과를 함수를 호출한 곳으로 보내준다.
* 왜 쓰냐면 연산한 결과를 다른곳에 사용하기 위함
* 처음에 console만 보면 동일해서 헷갈림.

```python
def plus(val1, val2):
    return val1 + val2

result = plus(10, 20)

print(result)
```
plus()를 호출한 곳으로 값을 돌려준다.



