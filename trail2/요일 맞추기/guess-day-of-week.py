m1, d1, m2, d2 = map(int, input().split())

#                  1.  2.  3.  4.  5.  6.  7.  8.  9. 10. 11. 12.
num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day_of_week = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']

first_days = sum(num_of_days[0:m1])+d1
goal_days = sum(num_of_days[0:m2])+d2

min_day = goal_days - first_days
print(day_of_week[min_day % 7])

