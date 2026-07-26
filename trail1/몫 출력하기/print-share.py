cnt = 0
while True:
    if cnt < 3:
        number = int(input())
        if number % 2 == 0:
            print(number // 2)
            cnt += 1
    else:
        break