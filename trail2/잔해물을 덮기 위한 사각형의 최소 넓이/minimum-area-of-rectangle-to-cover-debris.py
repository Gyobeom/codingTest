import sys

# 좌표 입력 받기
x1, y1, x2, y2 = [0] * 2, [0] * 2, [0] * 2, [0] * 2
x1[0], y1[0], x2[0], y2[0] = map(int, input().split())
x1[1], y1[1], x2[1], y2[1] = map(int, input().split())

# 2차원 격자 및 오프셋 설정 (-1000 ~ 1000을 0 ~ 2000으로 변환)
matrix = [[0 for _ in range(2005)] for _ in range(2005)]
offset = 1000

def solution():
    # 1. 첫 번째 직사각형을 1로 채우기
    for x in range(x1[0] + offset, x2[0] + offset):
        for y in range(y1[0] + offset, y2[0] + offset):
            matrix[x][y] = 1
            
    # 2. 두 번째 직사각형을 0으로 덮어버리기 (잔해물 제거)
    for x in range(x1[1] + offset, x2[1] + offset):
        for y in range(y1[1] + offset, y2[1] + offset):
            matrix[x][y] = 0

    # 잔해물(1)이 있는 영역의 경계값 초기화
    min_x, max_x = 2005, -1
    min_y, max_y = 2005, -1
    exist = False

    # 3. 격자를 순회하며 남은 잔해물의 최소/최대 좌표 구하기
    for x in range(2005):
        for y in range(2005):
            if matrix[x][y] == 1:
                exist = True
                if x < min_x: min_x = x
                if x > max_x: max_x = x
                if y < min_y: min_y = y
                if y > max_y: max_y = y

    # 잔해물이 하나도 없다면 최소 넓이는 0
    if not exist:
        return 0
        
    # 4. 잔해물을 감싸는 최소 직사각형의 넓이 계산
    # 격자의 한 칸은 크기가 1이므로 (최대좌표 - 최소좌표 + 1)이 실제 길이가 됩니다.
    width = max_x - min_x + 1
    height = max_y - min_y + 1
    
    return width * height

print(solution())