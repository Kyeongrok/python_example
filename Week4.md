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