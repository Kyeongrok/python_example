def gugudan(dan):
    for num1 in range(1, 9+1):
        result = "{} * {} = {}".format(dan, num1, dan * num1)
        print(result)

for dan in range(2, 9 + 1):
    gugudan(dan)
