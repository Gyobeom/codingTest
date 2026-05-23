N = int(input())
numbers = list(map(int,input().split()))
numbers.reverse()
for i in numbers:
    if i % 2 == 0:
        print(i,end=' ')