N = int(input())

data_list = []
for _ in range(N):
    data_list.append(int(input()))

sum = 0
for data in data_list:
    if data % 2 != 0 and data % 3 == 0:
        sum += data
print(sum)
