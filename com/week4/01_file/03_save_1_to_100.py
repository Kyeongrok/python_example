file_name = "./1_to_100.txt"
f1 = open(file_name, mode='w+')
for number in range(1, 101):
    f1.write(str(number) + "\n")
f1.close()
print("파일 저장이 완료 되었습니다. 같은 폴더에 {}를 찾아보세요.".format(file_name))