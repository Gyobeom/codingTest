number_list = [list(map(int,input().split()))for _ in range(4)]
tot = 0
for y in range(4):
    for x in range(y+1):
        tot += number_list[y][x]
print(tot)
