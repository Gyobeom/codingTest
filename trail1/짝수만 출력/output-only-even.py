A, B = map(int, input().split())

while(A < B + 1):
    if A % 2 == 0:
        print(A, end = ' ')
    A += 1