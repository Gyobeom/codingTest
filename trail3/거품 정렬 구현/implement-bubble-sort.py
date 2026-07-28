n = int(input())
number_list = list(map(int,input().split()))

for i in range(n - 1):
    for j in range(n - 1 - i):
        if number_list[j] > number_list[j + 1]:
            tmp = number_list[j]
            number_list[j] = number_list[j+1]
            number_list[j+1] = tmp

print(*number_list)
