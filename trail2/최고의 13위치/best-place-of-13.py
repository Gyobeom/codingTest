n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
max_cnt = 0
for r in range(n):
    for c in range(n - 2):
        max_cnt = max(max_cnt, grid[r][c] + grid[r][c+1] + grid[r][c+2])
print(max_cnt)