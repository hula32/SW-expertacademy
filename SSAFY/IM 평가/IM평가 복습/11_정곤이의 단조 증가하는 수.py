T = int(input())

for t in range(1, T+1):
    N = int(input())
    A = list(map(int, input().split()))

    result = [] # [8, 14, 20, 28, 40, 70]
    for i in range(N-1):
        for j in range(i+1, N):
            result.append(A[i]*A[j])
    

    answer = -1
    for r in result:
        s = str(r)
        ok = True
        for i in range(len(s)-1):
            if s[i] > s[i+1]:
                ok = False
                break
        if ok:
            answer = max(answer, r)
    
    print(f'#{t} {answer}')






