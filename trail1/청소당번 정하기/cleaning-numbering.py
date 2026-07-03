n = int(input())
clean_cnt = [0,0,0]

for i in range(1,n + 1):
    if i % 12 == 0:
        clean_cnt[2] += 1
    elif i % 3 == 0:
        clean_cnt[1] += 1
    elif i % 2 == 0:
        clean_cnt[0] += 1
print(clean_cnt[0], clean_cnt[1], clean_cnt[2])