n = int(input())
numbers = []
for i in range(n):
    numbers.append((map(int,input().split())))

for a,b in numbers:
    tot = 0
    for a in range(a,b+1):
        if a % 2 == 0:
            tot += a
        
    print(tot)
