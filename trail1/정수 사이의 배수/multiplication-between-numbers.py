A, B = map(int,input().split())

sum = 0
cnt = 0
for i in range(A, B + 1):
    if i % 5 == 0 or i % 7 == 0:
        cnt += 1
        sum += i

print(f'{sum} {sum / cnt:.1f}')