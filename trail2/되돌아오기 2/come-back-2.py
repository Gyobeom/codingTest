commands = input()

# Please write your code here.

# 조건들
# 북쪽을 향한 상태
# 명령 L이 주어지면 왼쪽으로 90도 전환 R이 주어지면 오른쪽으로 90도 방향 전환 
# 명령 F면 바라보는 방향으로 한칸 이동

def solution():
    # 북동남서
    dxs, dys = [-1,0,1,0],[0,1,0,-1]
    # 처음 북쪽 방향
    dir = 0
    # 초기값 설정
    x, y = 0 , 0
    time_cnt = 0

    for i in range(len(commands)):
        if commands[i] == 'L':
            dir = (dir - 1) % 4
        elif commands[i] == 'R':
            dir = (dir + 1) % 4
        else:
            x, y = x + dxs[dir], y + dys[dir]
        time_cnt += 1
        if x == 0 and y == 0:
            return time_cnt
    return -1

print(solution())
            