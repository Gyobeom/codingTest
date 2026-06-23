n = 3
arrs = [(row[0], int(row[1])) for row in [input().split() for _ in range(n)]]

cnt = 0

for i in range(len(arrs)):
    if arrs[i][0]== 'Y' and int(arrs[i][1]) >= 37:
        cnt += 1
if cnt >= 2:
    print('E')
else:
    print('N')

