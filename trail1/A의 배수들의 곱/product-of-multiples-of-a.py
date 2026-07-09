A, B = map(int,input().split())

mul_val = 1
for i in range(1, B + 1):
    if i % A == 0:
        mul_val *= i
print(mul_val) 