# 실습2 2단을 출력 해보세요
'''
ex)
2 * 1 = 2
2 * 2 = 4
...
2 * 9 = 18

hint)
for문
formatting
'''

for num in range(1, 10):
    result = "{} * {} = {}".format(2, num, 2 * num)
    print(result)
