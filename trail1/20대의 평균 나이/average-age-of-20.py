up_20_check = False
age_list = []

while True:
    age = int(input())
    if age > 19 and age < 30:
        age_list.append(age) 
    else:
        print(f'{sum(age_list) / len(age_list):.2f}')
        break
