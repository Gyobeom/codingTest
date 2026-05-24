a_numbers = [list(map(int,input().split())) for _ in range(3)]
input()
b_numbers = [list(map(int,input().split())) for _ in range(3)]

for y in range(3):
    for x in range(3):
        result = a_numbers[y][x] * b_numbers[y][x]
        print(result,end=' ')
    print()