# 10 + 20, 20 * 30 을 출력 하고
# 각각의 결과를 나눈(/) 값도 출력 해보세요.

def plus(val1, val2):
    return val1 + val2
def multiple(val1, val2):
    return val1 * val2
def divide(val1, val2):
    return val1 / val2

result_plus = plus(10, 20)
result_multiple = multiple(20, 30)
result_divide = divide(result_plus, result_multiple)

print(result_plus)
print(result_multiple)
print(result_divide)