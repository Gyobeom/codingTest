n = int(input())

num_list = [[0 for i in range(n)] for i in range(n)]

for x in range(n):
    if x % 2 == 0:
        for y in range(n):
            num_list [y][x] = y + 1
    else:
        for y in range(n):
            num_list[y][x] = n - y

for y in range(n):
    for x in range(n):
        print(num_list[y][x],end='')
    print()