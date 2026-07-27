N = int(input())
schedule_list = []

for _ in range(N):
    schedule_list.append(list(map(int,input().split())))

schedule_list.sort(key=lambda x: x[0])
max_val = 0

for i in range(N):
    before_end, total_sum = 0, 0
    for j in range(N):
        if i == j:
            continue
        else:
            start, end = schedule_list[j][0], schedule_list[j][1]
            # start가 이전 종료 값보다 클 경우
            if start >= before_end:
                total_sum += end - start
            # start가 이전 종료 값보다 작을 경우 
            else:
                total_sum += end - start - (before_end - start) 
        before_end = end
    max_val = max(max_val, total_sum)
print(max_val)
