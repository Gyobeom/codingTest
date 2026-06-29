a = input()
max = 0
# Please write your code here.
sum = 0
for i in range(len(a)):
    for k in range(len(a)):
        # 0일 때 변경 해서 해야함. 
        if i == k:
            if a[k] == '0':
                sum += 2 ** (len(a) - (k + 1))
                continue
            elif a[k] == '1':
                continue
        elif a[k] == '1':
            sum += 2 ** (len(a) - (k + 1))
    if sum > max:
        max = sum
    sum = 0

print(max)


