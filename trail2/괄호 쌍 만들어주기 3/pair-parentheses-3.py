A = input()

# Please write your code here.

sum_cnt = 0

for i in range(len(A)-1):
    if A[i] == '(':
        for j in range(i+1, len(A)):
            if A[j] == ')':
                sum_cnt += 1
print(sum_cnt)