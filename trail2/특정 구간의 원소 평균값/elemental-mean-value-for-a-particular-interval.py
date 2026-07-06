n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
# 특정 구간을 잡았을 때, 그 구간 안에 있는 원소 평균 값이 그 구간의 원소 중 하나가 되는 서로 다른 가짓 수
# 완전 탐색 진행

tot_cnt = 0
for i in range(n):
    for j in range(i, n):
        cnt_list = []
        for k in range(i, j + 1):
            cnt_list.append(arr[k])
        if sum(cnt_list) / len(cnt_list) in cnt_list:
            tot_cnt += 1
print(tot_cnt)