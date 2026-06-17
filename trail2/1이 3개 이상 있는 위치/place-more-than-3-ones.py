n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

#동서남북
dxs, dys = [1,0,-1,0], [0,-1,0,1]

#결과 저장
total_cnt = 0


# 좌표 밖 벗어 나는지 검사
def in_range(x,y):
    return 0 <= x and x < len(grid) and 0 <= y and y < len(grid[0])

for x in range(len(grid)):
    for y in range(len(grid[x])):
        cnt = 0
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx , y + dy
            if in_range(nx, ny) and grid[nx][ny] == 1:
                cnt += 1
        if cnt >= 3:
            total_cnt += 1

print(total_cnt)