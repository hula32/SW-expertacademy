while True:
    word = input().strip()
    word = word.lower()
    
    if word == '#':
        break
    
    cnt = 0
    for w in word:
        if w == 'a' or w == 'e' or w == 'i' or w == 'o' or w == 'u' :
            cnt += 1

    print(cnt)

# 완료

