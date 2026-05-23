a, b = map(int,input().split())
tot = 0
for i in range(a,b+1):
    if i % 2 == 0:
        tot += i
print(tot)