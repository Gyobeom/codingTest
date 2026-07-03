n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.

max_result = 0
# K 개수 만큼 반복 할 수 있도록 지정
for i in range(n - k + 1):
    result = 0
    for j in range(i, i + k):
        result += arr[j]
    max_result = max(max_result,result)
print(max_result)