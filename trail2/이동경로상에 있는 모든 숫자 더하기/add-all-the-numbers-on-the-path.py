N, T = map(int, input().split())
str = input()
board = [list(map(int, input().split())) for _ in range(N)]

# Please write your code here.

# L,R,F 왼쪽 90도, 오른쪽 90도, F는 한칸이동
# 가운데에서 시작
# 처음에는 북쪽을 바라봄

def solution():
    # 북,동,남,서
    dxs, dys = [-1,0,1,0], [0,1,0,-1]
    # 북에서 시작
    dir = 0
    # 초기 가운데 좌표값 세팅
    x, y = N // 2, N // 2
    # 초기값 세팅
    result = board[x][y]

    def in_range(x,y):
        return 0 <= x and x < N and 0 <= y and y < N

    for i in range(T):
        # 방향 설정 오른쪽/왼쪽
        if str[i] == 'R':
            dir = (dir + 1) % 4
        elif str[i] == 'L':
            dir = (dir - 1) % 4
        elif str[i] == 'F':
            nx,ny = x + dxs[dir], y + dys[dir]
            if not in_range(nx, ny):
                continue
            x, y = nx, ny
            result += board[x][y]
    return result
print(solution())



    
