n, t = map(int, input().split())
r, c, d = input().split()
r, c = int(r), int(c)

# Please write your code here.

mapper = {
    'R':0,
    'D':1,
    'U':2,
    'L':3
}


# 반대 방향으로 뒤집히는 경우를 참고 해서 3을 빼면 반대가 되도록 설정했음 0,3 / 1,2
dx, dy = [0,1,-1,0],[1,0,0,-1]

def in_range(x,y):
    return 0 <= x and x < n and 0 <= y and y < n

# 
def solution():
    now_t = 0
    x, y = r - 1, c - 1
    dir = mapper[d]
    while now_t < t:
        # 정상 일 때, 한칸 이동
        nx, ny = x + dx[dir], y + dy[dir]
        if in_range(nx,ny):
            x,y = nx,ny
        else:
            # 벗어났을 때 방향 전환
            dir = 3 - dir
        now_t += 1
    return (x+1,y+1)
x,y = solution()
print(x,y)