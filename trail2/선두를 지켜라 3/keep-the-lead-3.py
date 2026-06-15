N, M = map(int, input().split())

# Process A's movements
v = []
t = []
for _ in range(N):
    vi, ti = map(int, input().split())
    v.append(vi)
    t.append(ti)

# Process B's movements
v2 = []
t2 = []
for _ in range(M):
    vi, ti = map(int, input().split())
    v2.append(vi)
    t2.append(ti)

# Please write your code here.
# 우선순위를 계속 확인해야함. 어떻게 바교? 고민 필요


def saveResult(goal_idx, v, t, result):
    sum = 0
    for i in range(goal_idx):
        for _ in range(t[i]):
            sum += v[i]
            result.append(sum)
    return result


def solution():
    a_history = saveResult(N,v,t,[])
    b_history = saveResult(M,v2, t2, [])

    top = [0,0] #초기값 
    cnt = 0
    # 조건 a가 높으면 top[0] =1 b가 높으면 [1] = 1
    for i in range(len(a_history)):
        # a가 b보다 크면서 전당에 없을 때
        if a_history[i] > b_history[i] and (top[0] == 0 or sum(top) == 2):
            top[1] = 0
            top[0] = 1
            cnt += 1
        # b가 a보다 크면서 전당에 없을 때
        elif b_history[i] > a_history[i] and (top[1] == 0 or sum(top) == 2):
            top[0] = 0
            top[1] = 1
            cnt += 1
        elif a_history[i] == b_history[i] and top[0] + top[1] < 2:
            top[0] = 1
            top[1] = 1
            cnt += 1
       
    return cnt
print(solution())
