N, M = map(int, input().split())
arr = [input() for _ in range(N)]

# Please write your code here.
# 사방, 대각선 전부 확인 해야함
# 확인 시에, 맵을 벗어나면 확인 X

# 왼쪽 위 대각선 - row -1 / col -1 
# 왼쪽 아래 대각선 - row + 1/ col -1
# 오른쪽 위 대각선 - row - 1 / col +1
# 오른쪽 아래 대각선 - row + 1 / col +1

# 왼쪽 - row 0 / col -1
# 오른쪽 - row 0 / col +1
# 위 - row +1 / col 0
# 아래 - row - 1 / col 0

answer_word = ['LEE']

def check_word(x,y,dir):
    r_dir = []
    c_dir = []
    if dir == 'cross':
        #대각선 방향 순차적으로 왼쪽 위 -> 오른쪽 위, 오른쪽 아래, 왼쪽 아래 시계 방향순으로 지정
        r_dir = [-1,-1,1,1]
        c_dir = [-1,1,1,-1]
    else: 
        # 상,우,하,좌 방향으로 시계 방향순 
        r_dir = [1,0,-1,0]
        c_dir = [0,1,0,-1]       

    tot_cnt = 0
    for i in range(4):
        #초기 시작 값 넣기
        total_word = arr[x][y]
        nx, ny = x, y
        for _ in range(2):
            nx,ny = nx + r_dir[i], ny + c_dir[i]
            #범위 벗어남
            if nx < 0 or nx > N - 1 or ny < 0 or ny > M - 1:
                break
            total_word += arr[nx][ny]
        if total_word in answer_word:
            tot_cnt += 1
    return tot_cnt


# 전체 배열 반복 
total_cnt = 0
for r in range(N):
    for c in range(M):
        #시작과 끝인 L|E일 경우에만 검토 진행
        if arr[r][c] in ['L']:
            cross_dir_cnt = check_word(r,c,'cross')
            line_dir_cnt = check_word(r,c,'line')
            total_cnt += cross_dir_cnt + line_dir_cnt
print(total_cnt)
     
