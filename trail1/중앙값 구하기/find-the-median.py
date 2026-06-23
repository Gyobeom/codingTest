A,B,C = map(int,input().split())


if (A <= B <= C) or (C <= B <= A):
    median = B
elif (B <= A <= C) or (C <= A <= B):
    median = A
else:
    median = C

print(median)