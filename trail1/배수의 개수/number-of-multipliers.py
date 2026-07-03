first_cnt = 0
second_cnt = 0
for _ in range(10):
    value = int(input())
    if value % 3 == 0:
        first_cnt += 1
    if value % 5 == 0:
        second_cnt += 1
print(first_cnt, second_cnt)