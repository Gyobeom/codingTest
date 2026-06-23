a, b, c = map(int,input().split())

max_val = a

if b > max_val:
    max_val = b

if c > max_val:
    max_val = c

print(max_val)
    