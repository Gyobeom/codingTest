n, k = map(int, input().split())
x = []
c = []
for _ in range(n):
    pos, char = input().split()
    x.append(int(pos))
    c.append(char)

# 초기 값 1 설정 H인 경우에만 2로 지정
lines = [0] * 20000
for i in range(n):
    if c[i] == 'G':
        lines[x[i]] = 1
    elif c[i] == 'H':
        lines[x[i]] = 2
result_max = 0
for i in range(1,len(lines) - (k + 2)):
    result_sum = 0
    for j in range(i, i + k + 1):
        result_sum += lines[j]
    result_max = max(result_max, result_sum)
print(result_max)


# Please write your code here.