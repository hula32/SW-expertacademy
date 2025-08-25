T = int(input())

for t in range(1, T+1):
    N = int(input()) # 3
    A = list(map(int, input().split())) # 000
    B = list(map(int, input().split())) # 010

    answer = 0

    for i in range(N): # 0,1,2
        if A[i] != B[i]:
            answer += 1
            for j in range(i, N):
                A[j] = (A[j]+1) % 2
    
    print(f'#{t} {answer}')
