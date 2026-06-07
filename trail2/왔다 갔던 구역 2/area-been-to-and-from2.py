n = int(input())
x = []
dir = []
for _ in range(n):
    xi, di = input().split()
    x.append(int(xi))
    dir.append(di)

# Please write your code here.
idx = 100
visit_list = [0] * 200

for x, dir in zip(x,dir):
    if dir == 'L':
        goal = -(x) + idx
        for i in range(goal, idx):
            visit_list[i] += 1
        idx = goal

    else:
        goal = x + idx
        for i in range(idx,goal):
            visit_list[i] += 1
        idx = goal

cnt = 0
for i in visit_list:
    if i >= 2:
        cnt += 1
print(cnt)


