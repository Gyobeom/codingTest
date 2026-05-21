m1, d1, m2, d2 = map(int, input().split())
A = input()

num_of_days = [0,31,29,31,30,31,30,31,31,30,31,30,31]
# Please write your code here.

first_days = sum(num_of_days[0:m1])+ d1
goal_days = sum(num_of_days[0:m2]) + d2
min_days = goal_days - first_days

div_days = int(min_days / 7)
rest = min_days % 7

total_cnt = div_days

if A == 'Mon' and rest >= 0:
    total_cnt += 1
elif A == 'Tue' and rest >= 1:
    total_cnt += 1
elif A == 'Wed' and rest >= 2:
    total_cnt += 1
elif A == 'Thu' and rest >= 3:
    total_cnt += 1
elif A == 'Fri' and rest >= 4:
    total_cnt += 1
elif A == 'Sat' and rest >= 5:
    total_cnt += 1
elif A == 'Sun' and rest >= 6:
    total_cnt += 1

print(total_cnt)