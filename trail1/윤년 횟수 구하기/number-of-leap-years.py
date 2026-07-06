tot_cnt = 0
N = int(input())
for i in range(1, N + 1):
    if i % 4 == 0:
        if i % 100 == 0 and i % 400 != 0:
            continue
        else:
            tot_cnt += 1
        
    

print(tot_cnt)
