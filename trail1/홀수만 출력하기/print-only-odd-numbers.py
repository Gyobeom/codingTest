N = int(input())
data_list = []

for _ in range(N):
    value = int(input())
    data_list.append(value)

for number in data_list:
    if number % 3 == 0 and number % 2 != 0:
        print(number)
