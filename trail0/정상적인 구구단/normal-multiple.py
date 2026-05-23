n = int(input())
for y in range(1,n+1):
    for x in range(1,n+1):
        print(f'{y} * {x} = {y*x}',end='')
        if x < n:
            print(', ',end='')
    print()