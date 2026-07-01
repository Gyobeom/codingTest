n = int(input())
arr = [int(input()) for _ in range(n)]

# Please write your code here.
# 반복문을 통해서 1 -> 1-n -> 1-n-n 이런식으로 구해야 함 
# carry 계산이 별도로 들어가야 함.

max = 0

# 자리수 carry 구하는 함수
def calculate_carry(numbers:[]):
    sum = [0,0,0,0,0]
    for number in numbers:
        cnt = 0
        if number < 10:
            sum[cnt] += number
            continue
        while number != 0:
            q = number // 10
            r = number % 10
            sum[cnt] += r
            if sum[cnt] > 9:
                return True
            number = q
            cnt += 1
    return False

for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            is_carry = calculate_carry([arr[i],arr[j],arr[k]])
            if is_carry == False:
                total_sum = arr[i] + arr[j] + arr[k]
                max = total_sum if max < total_sum else max
if max == 0:
    print(-1)
else:
    print(max)
            