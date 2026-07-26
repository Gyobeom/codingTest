n = int(input())
point_list = []
for _ in range(n):
    point_list.append(list(map(int,input().split( ))))

distance_list = []
for i in range(n - 1):
    for j in range(i + 1, n):
        distance = pow(point_list[i][0] - point_list[j][0], 2) + pow(point_list[i][1] - point_list[j][1],2)
        distance_list.append(distance)

print(min(distance_list))
