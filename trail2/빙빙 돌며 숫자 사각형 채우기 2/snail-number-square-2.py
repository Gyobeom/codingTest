n, m = map(int, input().split())

# Please write your code here.
# 남, 동, 복, 서 방향으로 돌면서 사각형 채우기 
# 초기에 0으로 모든 보드를 설정 하고 이후 방문 시에, 0이 아니면서 보드 밖이 아닐 경우에만 삽입

def solution():
    # 0으로 빈 배열 생성
    board = [[0 for _ in range(m)] for _ in range(n)]
    # 순회 방향에 따른 순서 남, 동, 북, 서
    dxs, dys = [1,0,-1,0], [0,1,0,-1]
    
    # 초기 방향, 및 x, y 값 설정
    dir = 0 
    x, y = 0, 0
    board[x][y] = 1

    def in_range(x, y):
        return 0 <= x and x < n and 0 <= y and y < m

    for i in range(2, n * m + 1):
        nx, ny = x + dxs[dir], y + dys[dir]
        if not in_range(nx,ny) or board[nx][ny] != 0:
            dir = (dir + 1) % 4

        x, y = x + dxs[dir], y + dys[dir]
        board[x][y] = i
    return board

board = solution()
for i in range(n):
    for j in range(m):
        print(board[i][j], end = ' ')
    print()
