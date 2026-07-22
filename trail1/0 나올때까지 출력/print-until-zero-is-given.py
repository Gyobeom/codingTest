num_history = []
while True:
    N = int(input())
    if N <= 0:
        for num in num_history:
            print(num)
        break
    else:
        num_history.append(N)