B, A = map(int,input().split())

while B >= A:
    if B % 2 == 0:
        print(B, end = ' ')
    B -= 1