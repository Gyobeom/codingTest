number_list = [list(map(int,input().split())) for _ in range(4)]
cnt = 0
for y in range(4):
    for x in range(4):
        if int(number_list[y][x]) % 5 == 0:
             cnt += 1
print(cnt)
