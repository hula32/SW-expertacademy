# 큐 자료구조 생각나야함

T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())
    N_list = list(map(int, input().split()))

    A = M % N # 작업횟수 -> 1

    for i in range(A):
        N_list.append(N_list.pop(0))

    
    print(f'#{t} {N_list[0]}')

    



