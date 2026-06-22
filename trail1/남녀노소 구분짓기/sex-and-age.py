gender = int(input())
age = int(input())

if gender == 0:
    if age < 19:
        print('BOY')
    else:
        print('MAN')
else:
    if age < 19:
        print('GIRL')
    else:
        print("WOMAN")