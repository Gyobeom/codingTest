import sys
n = int(input())
A = list(map(int, input().split()))

# Please write your code here.
MIN_SIZE = sys.maxsize
MAX_SIZE = -sys.maxsize

max_sum = MIN_SIZE
for i in range(n):
    sum_diff = 0
    for j in range(n):
        if i == j:
            continue
        else:
            sum_diff += abs(int(i-j)) * A[j]
    if sum_diff < max_sum:
        max_sum = sum_diff
print(max_sum)
