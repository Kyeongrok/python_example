#구구단 3단 출력하기
x = range(1, 9)

def print_dan(dan):
    for item in x:
        print("{}*{}={}".format(dan, item, dan * item))

for dan in range(2, 10):
    print_dan(dan)
