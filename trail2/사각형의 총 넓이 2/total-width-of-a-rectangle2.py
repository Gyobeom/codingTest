n = int(input())
x1, y1, x2, y2 = [], [], [], []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    x1.append(a)
    y1.append(b)
    x2.append(c)
    y2.append(d)

offset = 100
# Please write your code here.
matrix = [[0 for _ in range(201)] for _ in range(201)]
for i in range(n):    
    for x in range(x1[i] + offset ,x2[i] + offset):
        for y in range(y1[i] + offset,y2[i] + offset):
            matrix[x][y] = 1

result = 0 
for i in matrix:
    result += sum(i)
print(result)