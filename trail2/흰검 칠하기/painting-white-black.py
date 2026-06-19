n = int(input())
commands = [tuple(input().split()) for _ in range(n)]
x = []
dir = []
for num, direction in commands:
    x.append(int(num))
    dir.append(direction)

# Please write your code here.
# 현재칸 포함하여 타일 칠함 반복문 그대로 사용
# 타일 색은 덧칠해진다. 마지막으로 칠해진 색으로 변경
# 타일 하나가 순서 상관 없이 흰색, 검은색 2번이상 칠해지면 더 이상 색 변화 없음

idx = 1000
block_list = [[0,0,'Y'] for i in range(100000)]

for i in range(n):
    if dir[i] == 'L':
        goal = idx - x[i] + 1
        for y in range(goal, idx + 1):
            # 회색으로 변하지 않았을 경우에만
            if block_list[y][2] == 'G':
                continue
            else:
                # 흰색에 계속 더함
                block_list[y][0] += 1
                block_list[y][2] = 'W'
            #흰색, 검은색 2번씩 나왔을 경우 회색 처리
            if block_list[y][0] >= 2 and block_list[y][1] >= 2:
                block_list[y][2]='G'
                continue
        idx = goal
    else:
        goal = idx + x[i]
        for y in range(idx,goal):
             # 회색으로 변하지 않았을 경우에만
            if block_list[y][2] == 'G':
                continue
            else:
                # 검은색에 계속 더함
                block_list[y][1] += 1
                block_list[y][2] = 'B'
            #흰색, 검은색 2번씩 나왔을 경우 회색 처리
            if block_list[y][0] >= 2 and block_list[y][1] >= 2:
                block_list[y][2]='G'
                continue
        idx = goal - 1

white_cnt, black_cnt, gray_cnt = 0,0,0
for block in block_list:
    if block[2] == 'W':
        white_cnt += 1
    elif block[2] == 'B':
        black_cnt += 1
    elif block[2] == 'G':
        gray_cnt += 1

print(white_cnt, black_cnt, gray_cnt)
    





