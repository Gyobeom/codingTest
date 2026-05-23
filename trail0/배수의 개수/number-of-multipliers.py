thr_cnt = 0
five_cnt = 0
for i in range(10):
    number = int(input())
    if number % 3 == 0:
        thr_cnt += 1
    if number % 5 == 0:
        five_cnt += 1
        
print(thr_cnt, five_cnt)
