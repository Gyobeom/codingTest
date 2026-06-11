N = int(input())
arr = [int(input()) for _ in range(N)]

# Please write your code here.
def solution():
    max = 0
    cnt = 0
    # 한개일 경우 
    if N == 1:
        return 1
    for i in range(len(arr)):
        if i == 0:
            cnt += 1
        # 둘다 강제로 양수로 만든 후 양수 일 때
        elif arr[i] < 0 and arr[i-1] < 0:
            cnt += 1
        elif arr[i] > 0 and arr[i-1] > 0:
            cnt += 1
        #수가 다른 경우
        else:
            if max < cnt:
                max = cnt
            cnt = 1
    if max < cnt:
        max = cnt
    return max

print(solution())
