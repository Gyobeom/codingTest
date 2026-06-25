N = int(input())
A = list(map(int, input().split()))

# Please write your code here.
# 3중 반복문으로 돌면서 전체 순회 해야함.
def solution():
    cnt = 0
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                if A[i] <= A[j] <= A[k]:
                    cnt += 1
    return cnt
print(solution())