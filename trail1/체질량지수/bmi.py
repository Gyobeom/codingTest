h,w = map(int,input().split())
w_check = (10000 * w) / (h * h)
if w_check >= 25:
    print(f"{int(w_check)}")
    print('Obesity')
else:
    print(f"{int(w_check)}")