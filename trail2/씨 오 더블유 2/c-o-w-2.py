n = int(input())
S = input()
cnt = 0

# Please write your code here.
for i in range(n):
    if S[i] == 'C':
        for j in range(i+1, n):
            if S[j] == 'O':
                for k in range(j+1, n):
                    if S[k] == 'W':
                        cnt += 1
print(cnt)            