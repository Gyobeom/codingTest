n, m = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
# 색칠할 칸에서 동,서,남,북으로 범위 안에 있고, 색칠이 이미 되어 있는 칸이 3개인 경우 편안한 상태

def solution():
    #빈 칸 만들기
    board = [[0 for _ in range(n+1)] for _ in range(m+1)]
    dxs, dys = [0,1,0,-1], [1,0,-1,0]
    cnt = 0
    
    def in_range(x,y):
        return 0 <= x and x < n and 0 <= y and y < m

    def check_board(x,y):
        cnt = 0
        for i in range(4):
            nx, ny = x + dxs[i], y + dys[i]
            if in_range(nx,ny) and board[nx][ny] == 1:
                cnt += 1
        if cnt == 3:
            return True
        return False
    
    # -1 필요 배열에 맞추기 위해서
    # 먼저 색칠 후 주변 판단. 
    for x,y in points:
        board[x-1][y-1] = 1
        flexable_check = check_board(x-1,y-1)
        if flexable_check:
            print(1)
        else:
            print(0)
solution()

    