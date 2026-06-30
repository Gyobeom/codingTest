n = int(input())
numbers = list(map(int, input().split()))


max = 0
# Please write your code here.
for i in range(len(numbers)):
    for j in range(i + 2, len(numbers)):
        if max < numbers[i] + numbers[j]:
            max = numbers[i] + numbers[j]
print(max)