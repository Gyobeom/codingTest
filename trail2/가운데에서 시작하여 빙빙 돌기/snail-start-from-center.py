n = int(input())
grid = [[0] * n for _ in range(n)]


# 가운데 시작이 아닌 마지막 시작으로 진행
# 서, 북, 동, 남 순으로 순회 하면서 값 넣음
# 마지막 값 부터 -1을 해서 가운데에 1을 넣음
# Please write your code here.
def solution():
    # 서, 북, 동, 남
    dxs, dys = [0,-1,0,1],[-1,0,1,0]
    # 초기 값 세팅 서쪽, 제일 마지막수
    dir = 0
    x,y = n - 1, n - 1
    grid[x][y] = n * n

    def in_range(x, y):
        return 0 <= x and x < n and 0 <= y and y < n
        
    for i in range(n * n - 1, 0, -1):
        nx, ny = x + dxs[dir], y + dys[dir]
        if not in_range(nx, ny) or grid[nx][ny] != 0:
            dir = (dir + 1) % 4
        nx, ny = x + dxs[dir], y + dys[dir]
        grid[nx][ny] = i
        x, y = nx, ny

solution()

for x in range(n):
    for y in range(n):
        print(grid[x][y],end=' ')
    print()



