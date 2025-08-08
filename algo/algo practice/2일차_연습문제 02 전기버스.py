T = int(input())

def count_charge(K, N, M, m_list):

    cnt = 0
    idx = 0

    while idx < N:
        c_char = []
        for m in m_list:
            if idx < m and m <= idx+K:
                c_char.append(m)
        
        if idx + K >= N:
            return cnt
        if len(c_char) == 0:
            return 0
        else:
            idx = max(c_char)
            cnt += 1


for t in range(1, T+1):
    K, N, M = list(map(int, input().split()))
    M_list = list(map(int, input().split()))

    cnt = count_charge(K, N, M, M_list)

    print(f'#{t} {cnt}')
                  




