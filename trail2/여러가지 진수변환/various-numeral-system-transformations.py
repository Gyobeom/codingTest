N, B = map(int, input().split())
digits = []

while True:
    if N < B:
        digits.append(N)
        break
    digits.append(N % B)
    N = N // B
for i in digits[::-1]:
    print(i,end='')


# Please write your code here.