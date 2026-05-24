N = input()
origin_num = 0
digits = []
# Please write your code here.
for i in range(len(N)):
    origin_num = origin_num * 2 + int(N[i])
origin_num *= 17

while True:
    if origin_num < 2:
        digits.append(origin_num)
        break
    digits.append(origin_num % 2)
    origin_num //= 2

for digit in digits[::-1]:
    print(digit,end='')

