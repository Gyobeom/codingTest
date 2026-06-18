N = int(input())
moves = [tuple(input().split()) for _ in range(N)]
dir = [move[0] for move in moves]
dist = [int(move[1]) for move in moves]

# Please write your code here.


def solution():
    dxs, dys = [0,1,0,-1], [1,0,-1,0]
    mapping = {
        'E':0,
        'S':1,
        'W':2,
        'N':3
    }
    x, y = 0,0
    time_cnt = 0 
    
    for i in range(N):
        now_dir = mapping[dir[i]]
        for _ in range(dist[i]):
            time_cnt += 1
            x,y = x + dxs[now_dir], y + dys[now_dir]
            if x == 0 and y == 0:
                return time_cnt
    return -1

print(solution())
