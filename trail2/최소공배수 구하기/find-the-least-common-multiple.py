n, m = map(int, input().split())

# Please write your code here.
cnt = 1
min = min([n,m])
max = max([n,m])
while True:
    if (min * cnt) % max  == 0:
        print(min * cnt)
        break
    cnt += 1 