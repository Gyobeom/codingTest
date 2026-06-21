a_age, a_male = map(str,input().split())
b_age, b_male = map(str,input().split())

def solution():
    if int(a_age) >= 19 and a_male == 'M':
        return 1
    elif int(b_age) >= 19 and b_male == 'M':
        return 1
    else:
        return 0
print(solution())