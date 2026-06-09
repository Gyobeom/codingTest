n = int(input())
commands = [tuple(input().split()) for _ in range(n)]
x = []
dir = []
for num, direction in commands:
    x.append(int(num))
    dir.append(direction)

# Please write your code here.
# 현재 타일을 포함 한다, 한방향으로 할거 기 때문에, L는 시작 위치에 + 1 하고 도착점 + 1로 반복문
# 왼쪽은 흰색, 오른쪽은 검은색 

tile_list = [0] * 10000
st_idx = 5000
for i in range(n):
    if dir[i] == 'L':
        lst_idx = st_idx - x[i] + 1
        for idx in range(lst_idx, st_idx+1):
            tile_list[idx] = 1

        st_idx = lst_idx
    else:
        goal_idx = st_idx + x[i]
        for idx in range(st_idx, goal_idx):
            tile_list[idx] = 2

        st_idx = goal_idx - 1

w = 0
b = 0
for tile in tile_list:
    if tile == 1:
        w += 1
    elif tile == 2:
        b += 1
print(w,b)
