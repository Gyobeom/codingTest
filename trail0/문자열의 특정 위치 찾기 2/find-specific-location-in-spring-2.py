words = ['apple','banana','grape','blueberry','orange']
find_word = input()
cnt = 0

for word in words:
    if find_word in word[2:4]:
        print(word)
        cnt += 1
print(cnt)