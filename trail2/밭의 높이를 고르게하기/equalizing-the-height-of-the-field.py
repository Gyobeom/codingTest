import sys
N, H, T = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
# 밭이 주어지고, 소모되는 비용 1 있음, 소모되는 비용은 최소로 하면서 연속하게 T의 값이 나와야 함. 
# 목표 값인 H 보다 높거나, 낮은 경우의 조건으로 -, + 진행
# T 만큼 연속 되어야 하니, 반복문은 해당 값을 뺀 값 까지만 진행
MIN_CNT = sys.maxsize
for i in range(N - T + 1):
    cnt_val = 0
    for j in range(i, i + T):
        #목표 값 보다 작을 때
        if arr[j] < H:
            cnt_val += H - arr[j]
        #목표 값 보다 높을 때
        elif arr[j] > H:
            cnt_val += arr[j] - H
        else:
            continue
    MIN_CNT = min(MIN_CNT,cnt_val)

print(MIN_CNT)
