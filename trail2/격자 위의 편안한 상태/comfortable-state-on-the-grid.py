import sys

def solution():
    # n: 격자 크기(N x N), m: 색칠 횟수
    line1 = sys.stdin.readline().split()
    if not line1: return
    n, m = map(int, line1)
    
    # N x N 격자이므로, 열의 크기도 n+1이어야 합니다.
    board = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    
    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
    
    def in_range(x, y):
        return 1 <= x <= n and 1 <= y <= n

    def check_board(x, y):
        cnt = 0
        for i in range(4):
            nx, ny = x + dxs[i], y + dys[i]
            if in_range(nx, ny) and board[nx][ny] == 1:
                cnt += 1
        return cnt == 3
    
    for _ in range(m):
        x, y = map(int, sys.stdin.readline().split())
        board[x][y] = 1
        
        # 방금 색칠한 칸이 편안한지 확인
        if check_board(x, y):
            print(1)
        else:
            print(0)

solution()