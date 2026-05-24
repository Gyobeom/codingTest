number_list = [list(map(int,input().split())) for _ in range(4)]

for y in range(4):
    tot = 0
    for x in range(4):
        tot += number_list[y][x]
    print(tot)