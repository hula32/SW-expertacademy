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
    arr = [input().strip() for _ in range(N)]

    result = ''

    # 행검사
    for r in range(N):
        for c in range(N-M+1):
            s = arr[r][c:c+M]
            if s == s[::-1]:
                result = s
    # 세로 검사          
    if not result:
        for c in range(N):
            for r in range(N-M+1):
                temp = []
                for i in range(M):
                    temp.append(arr[r+i][c])
                s = ''.join(temp)
                if s == s[::-1]:
                    result = s
    print(f"#{t} {result}")

    


