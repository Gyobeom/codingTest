n = int(input())
x1, y1, x2, y2 = [], [], [], []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    x1.append(a)
    y1.append(b)
    x2.append(c)
    y2.append(d)

# Please write your code here.
offset = 100
matrix =  [[0 for _ in range(200)] for _ in range(200)]

def solution():
    for i in range(n):
        for x_idx in range(x1[i] + offset, x2[i] + offset ):
            for y_idx in range(y1[i] + offset, y2[i] + offset):
                if i % 2 == 0:
                    matrix[x_idx][y_idx] = 1
                else:
                    matrix[x_idx][y_idx] = 2

def getResult():
    total = 0
    for x_idx in range(len(matrix)):
        for y_idx in range(len(matrix[x_idx])):
            if matrix[x_idx][y_idx] == 2:
                total += 1
    return total

solution()
print(getResult()) 
