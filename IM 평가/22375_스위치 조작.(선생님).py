# 앞에부터 조작 -> 이걸로
# 뒤에부터 조작 -> 안되는 이유: 앞에서 조작했던 부분이 사라짐
# 교차로 조작 -> 안되는 이유: 위와 동일

T = int(input())

for t in range(1, T+1):
    answer = 0
    N = int(input()) # 3
    A = list(map(int, input().split())) # 전
    B = list(map(int, input().split())) # 후

    for i in range(N): # 0, 1, 2
        if A[i] != B[i]:
            answer += 1
            for j in range(i, N): # 0~2, 1~2, 2
                A[j] = (A[j]+1)%2

    print(f'#{t} {answer}')
    