import sys
N, S = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
# 이중 반복문으로 순회 하면 2개씩 선택
# 최대 값 지정 후, 적은 값이면 대체 하도록
MIN_NUM = sys.maxsize
for i in range(N):
    for k in range(i + 1, N):
        total_sum = sum(arr) - arr[i] - arr[k]
        result = abs(total_sum - S)
        if result < MIN_NUM:
            MIN_NUM = result
print(MIN_NUM)