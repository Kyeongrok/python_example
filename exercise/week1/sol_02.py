# 10 + 20, 20 + 30 을 출력 하고
# 각각의 결과를 더한(+) 값도 출력 해보세요.

def plus(val1, val2):
    return val1 + val2

result_plus = plus(10, 20)
result_plus2 = plus(20, 30)
result_plus3 = plus(result_plus, result_plus2)

print(result_plus)
print(result_plus2)
print(result_plus3)


