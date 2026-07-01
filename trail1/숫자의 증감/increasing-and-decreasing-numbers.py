C, N = map(str,input().split())

if C == 'A':
    for i in range(1, int(N)+1):
        print(i,end=' ')
else:
    for i in range(int(N),0,-1):
        print(i, end = ' ')
