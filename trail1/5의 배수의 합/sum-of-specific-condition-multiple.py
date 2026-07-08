A, B = map(int,input().split())

sum_val = 0
big_num = 0
sm_num = 0
if A > B:
    big_num = A
    sm_num = B
else:
    big_num = B
    sm_num = A


for i in range(sm_num, big_num + 1):
    if i % 5 == 0:
        sum_val += i

print(sum_val)