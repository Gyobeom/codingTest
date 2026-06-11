n = int(input())
arr = [int(input()) for _ in range(n)]

# Please write your code here.
def solution():
    cnt = 0
    max = 0
    for i in range(len(arr)):
        if i == 0:
            cnt += 1
        elif arr[i] > arr[i-1]:
            cnt += 1
        else:
            if max < cnt:
                max = cnt
            cnt = 1
    if max < cnt:
        max = cnt
    return max

print(solution())
        