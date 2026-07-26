n = int(input())
points = []
for _ in range(n):
    points.append(list(map(int, input().split( ))))

min_square_size = 40000 * 40000
# 전체를 실행, 한 포인트씩 빼고 계산 진행 해서 제일 최소 직사각형 넓이 구하면 됨.
for i in range(n):
    x_val_list = []
    y_val_list = [] 
    # 포인트 제외 하고 나머지 값 진행
    for j in range(n):
        if i == j:
            continue
        x_val_list.append(points[j][0])
        y_val_list.append(points[j][1])

    x_length = max(x_val_list) - min(x_val_list)
    y_length = max(y_val_list) - min(y_val_list)

    if x_length == 0 or y_length == 0:
        min_square_size = 0
        break
    min_square_size = min(min_square_size, x_length * y_length)

print(min_square_size)
        