n, m = map(int, input().split())

d = []
t = []
for _ in range(n):
    direction, time = input().split()
    d.append(direction)
    t.append(int(time))

d2 = []
t2 = []
for _ in range(m):
    direction, time = input().split()
    d2.append(direction)
    t2.append(int(time))

# Please write your code here.
def pushRecord(goal_idx,d,t, record_arr):
    now = 0
    for i in range(goal_idx):
        if d[i] == 'R':
            for y in range(t[i]):
                now += 1
                record_arr.append(now)
        else:
            for y in range(t[i]):
                now -= 1
                record_arr.append(now)
    return record_arr

a_record = pushRecord(n,d,t,[0])
b_record = pushRecord(m,d2,t2,[0])

def check_arr(a_record, b_record):
    for i in range(1,min(len(a_record),len(b_record))):
        if a_record[i] == b_record[i]:
            return i
    return -1

print(check_arr(a_record,b_record))

    