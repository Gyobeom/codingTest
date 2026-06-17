n, m = map(int, input().split())
arr = [[0] * m for _ in range(n)]

# Please write your code here.
dxs, dys = [0,1,0,-1],[1,0,-1,0]

dir_num = 0
x, y = 0, 0

arr[x][y] = 1

def in_range(x,y):
    return 0 <= x and x < n and 0 <= y and y < m

for i in range(2, n * m +1):
    nx, ny = x + dxs[dir_num], y + dys[dir_num]

    # 좌표 안에 속하면서 미방문일 경우
    if not in_range(nx,ny) or arr[nx][ny] != 0:
        dir_num = (dir_num + 1) % 4

    x, y = x + dxs[dir_num], y + dys[dir_num]
    arr[x][y] = i

for i in range(n):
    for y in range(m):
        print(arr[i][y], end=' ')
    print()