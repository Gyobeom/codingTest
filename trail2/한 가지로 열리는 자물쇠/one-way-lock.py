N = int(input())
a, b, c = map(int, input().split())

# Please write your code here.
# 완전 탐색 진행 
cnt = 0
for i in range(1,N+1):
    for j in range(1,N + 1):
        for k in range(1, N + 1):
            if abs(a - i) <= 2 or abs(b - j) <= 2 or abs(k - c) <= 2:
                cnt += 1
print(cnt)
