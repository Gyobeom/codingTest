n = int(input())
num = 1
# 외부 반복
for i in range(n):
    #내부 반복
    for x in range(i+1):
        print(num,end=' ')
        num += 1
    print()