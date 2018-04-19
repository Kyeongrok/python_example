## 반복문(for문)
반복문은 내가 지정한 숫자의 범위만큼 반복을 하는 명령 입니다.
```python
for item in range(0, 10):
    print(item)
```

* for로 시작을 합니다. 한칸을 띄웁니다.
* item이라고 변수 이름을 씁니다. 한칸을 띄웁니다.
* in을 씁니다. 한칸을 띄웁니다. 뒤에 있는것 안에서 뽑아온다는 뜻입니다.
* range(0, 10)이라고 씁니다. 0 ~ 9까지 숫자 목록(list)을 만들어줍니다.
* :를 붙입니다.
* 엔터를 칩니다.
* print(item)을 입력합니다. item에 0부터 9까지 10개의 숫자가 들어옵니다.


## formatting
    * formatting은 특정 정보들을 포메팅 해서 출력하기 위해 사용합니다.
    * 여러가지 정보를 형식에 맞추어 한줄에 출력 하고 싶을 때 사용합니다. 
```python
print('greet:{} name:{}'.format('hello', 'kyeongork'))

result = '{} {}'.format('hello', 'kyeongrok2')
print(result)

gugudan = '{} * {} = {}'.format(2, 1, 2 * 1)
print(gugudan)
```

* 한줄에 여러가지 정보를 내가 원하는 모양으로 출력하기 위해 사용 합니다.


## 기본 개념과 용어들
    * url : 인터넷 주소
    * http : 인터넷 주소 앞에 붙는 것 protocol
    * html : 인터넷에서 문서를 보여줄때 쓰는 표현식들
    * server : 페이지를 서빙해주는 곳 (naver, google)

## 크롤링이란?
    * 인터넷 주소로 서버에 데이터를 요청해서 받아오는 것(콘솔에 출력하는 것)
    * 라이브러리 : urlopen

## 파싱이란?
    * 크롤링한 데이터에서 값을 뽑아내는 것
    * 라이브러리:bs4 BeautifulSoup 뷰티풀솝

css
css selector
	페이지 내에 데이터(한 단어)가 있는 곳의 주소
html tag

## 트리구조

<pre>
여행가는 책
책시작
	1장 비행기 타는 법
		1절 한국에서 가능법
		2절 외국에서 오는법
	2장 숙소로 이동 하는 법
책끝 맺음말
</pre>

```html
<html>
	<div>
		<ul>
			<li>
				<a>
					<span>
```

## html 태그
```html
<html>, <div>, <ul>, <li>, <a>, <span> 등이 있다.
```

# 실습
## week1
1. plus, minus, multiple, divide 함수 만들기(사칙연산)
    - 숫자 2개를 입력 받는 함수 4개를 만듭니다.
2.구구단 2단 출력하는 함수 만들기

## week2
1.구구단 2, 3단 출력하기
2.구구단 2 ~ 9단 출력하기

## week3
1. 0~99까지 숫자 만들기 arange
2. filter이용해서 80보다 큰 숫자 콘솔에 출력하기
3. data만들고 matplot으로 chart그리기
4. format()을 넣고 데이터 바로 가공 해보기 '00는 00입니다.'
5. matplot으로 차트 그리기
6. 1~10까지 우상향 하는 그래프를 그려보세요
7. linspace 사용하기
8. sin그래프 그리기
9. sin, cos그래프 한번에 그리기
10. y = x 함수 그래프로 그리기
11. y = x + 1 그래프로 그리기
12. 함수 x2는 x + 1인 함수를 만들어 보세요

## week4
1. file에 데이터 30개 만들어서 저장하기
2. file읽어서 list에 넣기
3. list를 가지고 chart그리기

## week5
13. pandas.DataFrame.to_csv로 dta 를 csv로 바꾸기
14. pandas.read_csv로 csv읽어오기

# 복습
## 복습1 function으로 parameter를 받아서 text출력하기
    안녕하세요 00님
    안녕히가세요 00님
    반갑습니다 00님
위에 3개의 string을 console에 출력하세요.

1. function 한개만 만들어서 출력 해보세요.
2. /review/week1/function_example_01.py

* 힌트
function하고 parameter를 사용 해야 합니다.

project root
project explorer에서 맨 위에 있는 것

## 복습2 return이 있는 function으로 사칙연산 만들기
    사칙연산 plus, minus, multiple, divide
    함수를 만들고
    
    10 + 20
    100 + 200
    20 - 30
    200 - 300
    30 * 40
    300 * 400
    40 / 50
    400 / 500
* 위 연산의 결과를 콘솔에 한번에 출력 할 수 있는 funciton을 만들어서 출력 해보세요.
* 출력 형태는 '결과는 00 입니다'

#### ex)
* 결과는 30 입니다.
* 결과는 300 입니다.

## 구구단 2 to 9단 출력하기
    1. 숫자2 출력하기
    2. 2 * 1 형태로 formatting해서 출력하기
    3. 반복문으로 2~9출력하기
    4. 2를 입력하면 2단이 출력되는 function만들기
    5. 위에서 만든 function을 2에서 9를 넣어서 출력하기