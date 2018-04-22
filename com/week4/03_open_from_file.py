f1 = open("./hello.txt", mode='r')
lines = f1.readlines()

datas = []
for line in lines:
    datas.append(line.replace("\n", ""))

print(datas)
