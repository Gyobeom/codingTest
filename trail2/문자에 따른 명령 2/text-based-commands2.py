dirs = input()

# Please write your code here.
# 동,남,서,북
dx,dy = [1,0,-1,0], [0,-1,0,1]
x, y = 0, 0
dir_num = 3
dir = ['N','E','S','W']


for dir in dirs:
    if dir == 'L':
        dir_num = (dir_num - 1) % 4
    elif dir == 'R':
        dir_num = (dir_num + 1) % 4
    else:
        x, y = x + dx[dir_num], y + dy[dir_num]

print(x, y)
