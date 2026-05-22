numbers = list(map(int,input().split()))

for i in range(10):
    if i > 1:
        sum_result = numbers[i-2]+numbers[i-1]
        if sum_result < 10 :
            numbers.append(sum_result)
        else:
            numbers.append(sum_result%10)
    print(numbers[i],end=' ')
    

