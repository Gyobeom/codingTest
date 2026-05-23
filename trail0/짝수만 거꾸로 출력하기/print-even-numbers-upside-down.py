N = int(input())
numbers = list(map(int,input().split()))

for i in range(N-1,-1,-1):
    if numbers[i] % 2 ==0:
        print(numbers[i],end=' ')
