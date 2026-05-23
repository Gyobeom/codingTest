n = 0
while n != 25:
    n = int(input())
    if n == 25:
        print('Good')
        break
    elif n < 25:
        print('Higher')
    else:
        print('Lower')

