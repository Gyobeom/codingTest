n = int(input())

for y in range(n):
    if y % 2 == 0:
        for x in range(1,n+1):
            print(x,end='')
    else:
        for x in range(n,0,-1):
            print(x,end='')
    print()