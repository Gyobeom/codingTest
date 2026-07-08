N = int(input())

sum_val = 0
for i in range(1, N):
    if N % i == 0:
        sum_val += i
if sum_val == N:
    print('P')
else:
    print('N')