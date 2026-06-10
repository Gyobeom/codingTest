n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x, y = zip(*points)
x, y = list(x), list(y)

# Please write your code here.
matrix = [[0 for _ in range(201)] for _ in range(201)]
offset = 100
for i in range(n):
    for x_idx in range(x[i] + offset,x[i]+8 + offset):
        for y_idx in range(y[i]+offset, y[i]+8+offset):
            matrix[x_idx][y_idx] = 1

total = 0
for i in matrix:
    total += sum(i)
print(total)
