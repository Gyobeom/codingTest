a, b = map(int, input().split())
tot = 0
# Please write your code here.
def isPrime(number):
    cnt = 0;
    for i in range(2, number):
        if number % i == 0:
            cnt += 1;
            if cnt >= 1:
                return False
    return True

for i in range(a,b+1):
    if isPrime(i):
        tot += i
print(tot)