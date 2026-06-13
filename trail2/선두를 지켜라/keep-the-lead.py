n, m = map(int, input().split())

# Process A's movements
v = []
t = []
for _ in range(n):
    vi, ti = map(int, input().split())
    v.append(vi)
    t.append(ti)

# Process B's movements
v2 = []
t2 = []
for _ in range(m):
    vi, ti = map(int, input().split())
    v2.append(vi)
    t2.append(ti)

# Please write your code here.
# a,b 각 시간 별로 이동한 result 배열 필요
def save_result(goal_idx, v_result, t_result, result):
    total_v = 0
    for i in range(goal_idx):
        for t in range(t_result[i]):
            total_v += v_result[i]
            result.append(total_v)
    return result


def solution():
    a_result = save_result(n, v, t, [0])
    b_result = save_result(m, v2, t2, [0])
    
    lead = ''
    cnt = -1

    for i in range(1, len(min(a_result,b_result))):
        if a_result[i] > b_result[i] and lead != 'a':
            lead = 'a'
            cnt += 1
        elif b_result[i] > a_result[i] and lead != 'b':
            lead = 'b'
            cnt += 1
    return(cnt)

print(solution())
