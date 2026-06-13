N, M, K = map(int, input().split())
student = [int(input()) for _ in range(M)]

# Please write your code here.
# 벌칙 카운트를 담을 배열이 필요 N번까지의 배열 필요
stu_cnt = [0 for _ in range(N+1)] 

def solution():
    for m in student:
        stu_cnt[m] += 1
        if stu_cnt[m] == K:
            return m
    return -1
print(solution())
