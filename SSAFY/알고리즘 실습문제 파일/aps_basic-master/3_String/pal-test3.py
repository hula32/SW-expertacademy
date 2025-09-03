
arr = [
"GOFFAKWFSM",
"OYECRSLDLQ",
"UJAJQVSYYQ",
"JAEZNNZEAQ",
"WJADCGSGCQ",
"WKUDGATDQL",
"JKGPFPYRKQ",
"TDCXBMQTIO",
"UNADRPQETZ",
"ZATWDEYDQF",
]

# print(arr[0][0])
# print(arr[1][0])
# print(arr[2][0])


N = 10
M = 4

for r in range(N):
    for c in range(N-M+1):
        lft = c
        rgt = c + M - 1

        pal = M // 2

        is_pal = True
        for k in range(pal):
            if arr[r][lft+k] != arr[r][rgt-k]:
                is_pal = False
        if is_pal:
            for i in range(lft, rgt+1):
                print(arr[r][i], end = '')
            print()

for c in range(N):
    for r in range(N-M+1):
        lft = r
        rgt = r + M - 1

        pal = M // 2

        is_pal = True
        for k in range(pal):
            if arr[lft+k][c] != arr[rgt-k][c]:
                is_pal = False
        if is_pal:
            for i in range(lft, rgt+1):
                print(arr[i][c], end = '')
            print()



# for c in range(N):

#     for r in range(N-M+1):
#         lft = r
#         rgt = r + M-1

#         is_pal = True

#         for step in range(num_pairs):
#             if arr[lft+step][c] != arr[rgt-step][c]:
#                 is_pal = False
        
#         if is_pal:
#             print(f"{lft}, {c} 위치에서 회문 발견")
#             for rr in range(lft, rgt+1):
#                 print(arr[rr][c], end='')
#             print()
    
