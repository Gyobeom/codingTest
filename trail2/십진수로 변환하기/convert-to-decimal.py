binary = list(map(int,input()))
tot = 0
# Please write your code here.
for x in range(len(binary)):
    tot = tot * 2 + binary[x]
print(tot)