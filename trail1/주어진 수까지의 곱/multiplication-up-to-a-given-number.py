A,B = map(int,input().split())
mul_val = 1
for i in range(A,B+1):
    mul_val *= i

print(mul_val)