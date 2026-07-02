A, B = map(int,input().split())

while A < B+1:
    print(A,end=' ')
    if A % 2 != 0:
        A *= 2
    elif A % 2 == 0:
        A += 3
