while True:
    w, h, word = map(str,input().split())
    print(int(w) * int(h))
    if word == 'C':
        break