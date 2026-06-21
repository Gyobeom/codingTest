a_math_score, a_eng_score = map(int,input().split())
b_math_score, b_eng_score = map(int,input().split())

if a_math_score > b_math_score:
    print('A')
elif b_math_score > a_math_score:
    print('B') 
elif a_math_score == b_math_score:
    if a_eng_score > b_eng_score:
        print('A')
    else:
        print('B')