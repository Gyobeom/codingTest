a, b, c = map(int,input().split())

min_val = (a if a < b else b) if (a if a < b else b) < c else c
print(min_val)