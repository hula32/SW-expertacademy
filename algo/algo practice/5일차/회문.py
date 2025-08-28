'''
3
10 10
GOFFAKWFSM
OYECRSLDLQ
UJAJQVSYYC
JAEZNNZEAJ
WJAKCGSGCF
QKUDGATDQL
OKGPFPYRKQ
TDCXBMQTIO
UNADRPNETZ
ZATWDEKDQF
'''

T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(input().strip()) for _ in range(N)]

    # 행 검사
    for r in range(N):
        for c in range(N-M+1):
            lft = c
            rgt = c + M -1

            pal = M // 2

            is_pal = True

            for step in range(pal):
                if arr[r][lft+step] != arr[r][rgt-step]:
                    is_pal = False
            if is_pal:
                print(f'#{t} ', end = '')
                for i in range(lft, rgt+1):
                    print(arr[r][i], end = '')
                print()

    
    for c in range(N):
        for r in range(N-M+1):
            lft = r
            rgt = r + M - 1

            pal = M // 2

            is_pal = True

            for step in range(pal):
                if arr[lft+step][c] != arr[rgt-step][c]:
                    is_pal = False

            if is_pal:
                print(f'#{t}', end=' ')
                for i in range(lft, rgt+1):
                    print(arr[i][c], end = '')
                print()

    


