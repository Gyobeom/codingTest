N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Please write your code here.
# 완전 탐색 진행

# M 만큼 확인하게끔 시작 값에서 -M
tot_cnt = 0
for i in range(N - M + 1):
    standard_list = B.copy()
    for j in range(i, i + M):
        if A[j] in standard_list:
            standard_list.remove(A[j])
    if len(standard_list) == 0:
        tot_cnt += 1
print(tot_cnt)
