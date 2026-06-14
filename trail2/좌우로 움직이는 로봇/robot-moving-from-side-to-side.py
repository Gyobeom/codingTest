n, m = map(int, input().split())

# Process robot A's movements
t = []
d = []
for _ in range(n):
    time, direction = input().split()
    t.append(int(time))
    d.append(direction)

# Process robot B's movements
t_b = []
d_b = []
for _ in range(m):
    time, direction = input().split()
    t_b.append(int(time))
    d_b.append(direction)

# Please write your code here.
# 정답은 직전 위치가 다르면서 현재 위치가 동일 할 경우
# 제외 조건 처음 같은


def save_move(goal_idx, t, d, result):
    move_cnt = 0
    for i in range(goal_idx):
        move = 1
        if d[i] == 'L':
            move *= -1
        for _ in range(t[i]):
            move_cnt += move
            result.append(move_cnt)
    return result


def solution():
    a_move_history = save_move(n, t, d, [0])
    b_move_history = save_move(m, t_b, d_b, [0])

    if len(a_move_history) < len(b_move_history):
        for _ in range(len(a_move_history), len(b_move_history)):
            a_move_history.append(a_move_history[-1])
    elif len(b_move_history) < len(a_move_history):
        for _ in range(len(b_move_history), len(a_move_history)):
            b_move_history.append(b_move_history[-1])

    before_check = False
    total_cnt = 0

    #개수 하나일 때 0 반환
    if len(a_move_history) == 1 and len(b_move_history):
        return 0

    #일반적인 순회를 돌면서 개수 확인
    for i in range(2, len(a_move_history)):
        if a_move_history[i] == b_move_history[i]:
            if a_move_history[i-1] != b_move_history[i-1]:
                total_cnt += 1
    # print(f'일반 순회 결과 값: {total_cnt}')
    return total_cnt

print(solution())


            

