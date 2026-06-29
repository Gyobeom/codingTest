import sys

n = int(input())
a = [int(input()) for _ in range(n)]

INT_MAX = sys.maxsize

# Please write your code here.

min = INT_MAX
for i in range(n):
    sum = 0
    now = i
    for j in range(0, n):
        sum += a[(now + 1) % n] * j
        now = now + 1
    if sum < min:
        min = sum
print(min)
