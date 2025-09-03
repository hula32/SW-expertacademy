T = int(input())

for t in range(1, T+1):
    N = int(input())
    number = list(map(int, input().split()))

    total = [] # [8, 14, 20, 28, 40, 70]
    for i in range(len(number)-1): # 0,1,2
        for j in range(i+1, len(number)): # 1,2,3
            total.append(number[i] * number[j])
    
    result = -1
    for to in total:
        s = str(to)
        is_ok = True
        for r in range(len(s)-1):
            if s[r] > s[r+1]:
                is_ok = False
                break
        if is_ok:
            result = max(result, to)

    print(f'#{t} {result}')


                            
        
