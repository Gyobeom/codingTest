n = int(input())
moves = [tuple(input().split()) for _ in range(n)]
dir = [move[0] for move in moves]
dist = [int(move[1]) for move in moves]

# Please write your code here.
dx, dy = [1,0,-1,0], [0,-1,0,1]

def solution():
    x,y = 0, 0
    for i in range(n):
        if dir[i] == 'E':
            x, y = x + dx[0] * dist[i], y + dy[0]
        elif dir[i] == 'S':
            x, y = x + dx[1], y + dy[1] * dist[i]
        elif dir[i] == 'W':
            x, y = x + dx[2] * dist[i], y + dy[2]
        else:
            x, y = x + dx[3], y + dy[3] * dist[i]
    return x,y
x,y = solution()
print(x,y)
    

