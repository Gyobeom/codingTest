MAX_NUM = 100
N, K = map(int, input().split())
candy = []
pos = []
candy_list = [0] * (MAX_NUM + 1)


# 좌표 값과 사탕이 주어지기에 0으로 초기화환 좌표 리스트에 사탕 값 넣어야함. 바구니의 위치는 최대 100개 이하로 생성
for _ in range(N):
    c, p = map(int, input().split())
    candy_list[p] += c

# if K >= 100:
#     print(sum(candy_list))

max_sum = 0
# 모든 좌표 값 다 확인 c-k, c+k 가 될 수 있도록 시작 값을 k 값으로 시작.
for i in range(MAX_NUM):
    sum_val = 0
    for j in range(i - K, i + K + 1):
        if j >= 0 and j <= MAX_NUM:
            sum_val += candy_list[j]
    max_sum = max(max_sum, sum_val)
print(max_sum)




