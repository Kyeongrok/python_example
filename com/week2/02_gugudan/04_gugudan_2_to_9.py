def print_gugudan(dan):
    for item in range(1, 10):
        print(dan, "*", item, "=", dan *item)

for dan in range(2, 10):
    print_gugudan(dan)


