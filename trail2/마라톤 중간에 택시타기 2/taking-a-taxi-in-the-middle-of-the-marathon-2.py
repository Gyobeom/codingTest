n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

# Please write your code here.
# 1번에서부터 모든 체크 포인트를 순선대로 방문 하고 N번 체크포인트에서 종료
# 중간에 있는 체크포인트를 하나 건너 뛰려고 한단 1번, N번 제외하고
# 최소 거리 구해야함.
# 거리 계산읜 택시 거리 x1-x2 + y1 - y2
# 중복 되는 체크포인트 있음 

min = 1000000
for i in range(1,n-1):
    sum = 0
    nx, ny = x[0], y[0]
    for k in range(1, n):
        if i == k:
            continue
        sum += abs(nx - x[k]) + abs(ny - y[k])
        nx,ny = x[k], y[k]
    if sum < min:
        min = sum
print(min)
