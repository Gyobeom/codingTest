n = int(input())
arr = [int(input()) for _ in range(n)]

# Please write your code here.

def solution():
    max = 0
    cnt = 0
    if n == 1:
        return 1
    for i in range(len(arr)):
        if i == 0 or arr[i] == arr[i-1]:
            cnt += 1
            if cnt > max:
                max = cnt
        elif arr[i] != arr[i-1]:
            if cnt > max:
                max = cnt
            cnt = 1
    return max
print(solution())