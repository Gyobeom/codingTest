mid_score, final_score = map(int,input().split())

if mid_score >= 90:
    if final_score >= 95:
        print(100000)
    elif final_score >= 90:
        print(50000)
    else:
        print(0)
else:
    print(0)