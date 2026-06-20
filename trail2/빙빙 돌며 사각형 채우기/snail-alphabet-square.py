n, m = map(int, input().split())

# Please write your code here.
# 회전 방향 동, 남, 서, 북
# 조건 Z 이후 다시 A 부터 반복 

def solution():
    board = [[0 for _ in range(m)] for _ in range(n)]
    dxs, dys = [0,1,0,-1], [1,0,-1,0]
    alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

    # 초기 값 설정
    dir = 0 
    x, y = 0, 0
    board[x][y] = alphabet[0]

    def in_range(x, y):
        return 0 <=x and x < n and 0 <= y and y < m

    for i in range(1, n * m):
        nx, ny = x + dxs[dir], y + dys[dir]
        # 좌표 벗어낫거나, 0이 아닐 경우 이미 존재
        if not in_range(nx,ny) or board[nx][ny] != 0:
            dir = (dir + 1) % 4
        
        x, y = x + dxs[dir], y + dys[dir]
        now_alphabet = i % len(alphabet)
        board[x][y] = alphabet[now_alphabet]
    return board

result = solution()

for i in range(n):
    for j in range(m):
        print(result[i][j],end = ' ')
    print()

