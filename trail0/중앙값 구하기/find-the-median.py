A, B, C = map(int,input().split())

if A < B:
    if B < C:
        print(B)
    else:
        print(C)
elif B < C:
    if C < A:
        print(C)
    else:
        print(A)
elif C < A:
    if A < B:
        print(A)
    else:
        print(B)
