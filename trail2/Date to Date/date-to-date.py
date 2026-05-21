m1, d1, m2, d2 = map(int, input().split())

# Please write your code here.
num_of_days = [0,31,28,31,30,31,30,31,31,30,31,30,31]


first_days = sum(num_of_days[0:m1]) + d1 
total_days = sum(num_of_days[0:m2]) + d2 + 1

print(total_days-first_days) 