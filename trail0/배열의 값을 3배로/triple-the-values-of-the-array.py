numbers = [list(map(int,input().split())) for _ in range(3)]
for y in range(len(numbers)):
    for x in range(len(numbers[y])):
        print(numbers[y][x]*3,end=' ')
    print()