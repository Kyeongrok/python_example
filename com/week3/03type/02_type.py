# 타입(형)

item = 2
print(type(item))

item2 = 2.0
print(type(item2))

item3 = "hello"
print(type(item3))

result = item + item2
print("item+item2:{}".format(result))
# result2 = item + item3
# print("item+item3:{}".format(result2))
result3 = item / 3
print("2 / 3:{}".format(result3))
print("type(2 / 3):{}".format(type(result3)))
# 4.0, 4, 계산이 안된다
# 2hello, error, error
# 0, float, 0.nnn, 0.65ee
