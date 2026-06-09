x1 = [0] * 3
y1 = [0] * 3
x2 = [0] * 3
y2 = [0] * 3

x1[0], y1[0], x2[0], y2[0] = map(int, input().split())
x1[1], y1[1], x2[1], y2[1] = map(int, input().split())
x1[2], y1[2], x2[2], y2[2] = map(int, input().split())

# Please write your code here.
offset = 1000
matrix = [[0 for _ in range(2001)] for _ in range(2001)]
for i in range(3):
    for x in range(x1[i] + offset,x2[i] + offset):
        for y in range(y1[i] + offset, y2[i] + offset):
            matrix[x][y] += i + 1

total_sum = 0
for row in matrix:
    for value in row:
        if value == 1 or value == 2:
            total_sum += 1
print(total_sum)
