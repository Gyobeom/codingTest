row,col = map(int,input().split())
a_list = [list(map(int,input().split()))for _ in range(row)]
b_list = [list(map(int,input().split()))for _ in range(row)]

for y in range(row):
    for x in range(col):
        if a_list[y][x] == b_list[y][x]:
            print(0,end = ' ')
        else:
            print(1,end= ' ')
    print()
