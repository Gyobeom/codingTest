a, b, c = map(int, input().split())

# Please write your code here.
start_min = 11 * 24 * 60 + 11 * 60 + 11
total_min = a * 24 * 60 + b * 60 + c

if total_min - start_min < 0 : 
    print(-1) 
else: 
    print(total_min - start_min)
