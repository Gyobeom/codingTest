start, end = map(int, input().split())
tot = 0
# Please write your code here.
for num  in range(start,end + 1):
    cnt = 0
    for i in range(1,num + 1):
        if num % i == 0:
            cnt += 1
    if cnt == 3:
        tot += 1
print(tot)
