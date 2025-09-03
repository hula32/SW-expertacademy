# text = "avaasdfabbadefcba"

# N = len(text)
# M = 4

# for idx in range(N-M+1): # 첫번째 문자의 idx
#     # 첫번째 문자의 index: idx
#     # 마지막 문자의 index: idx + 3
#     l = idx
#     r = idx + M - 1

#     num_pairs = M // 2

#     is_pal = True
#     for step in range(num_pairs):
#         if text[l + step] != text[r - step]:
#             is_pal = False
    
#     if is_pal:
#         print(f'{idx}번째 위치에서 회문 발견.')
#         for i in range(l, r+1):
#             print(text[i], end='')
#         print('')






# text = "avaasdfabbadefcba"

# N = len(text)
# M = 4

# for idx in range(N-M+1): # 전체 틀
#     l = idx
#     r = idx + M -1

#     pal = M // 2

#     is_pal = True
#     for i in range(pal) : # 세부적으로 돌기
#         if text[l+i] != text[r-i]:
#             is_pal = False

#     if is_pal: # 회문 찾았당
#         for t in range(l, r+1):
#             print(text[t], end = '')

#     print()



text = "avaasdfabbadefcba"

N = len(text)
M = 4

for idx in range(N-M+1): # 12-4+1=9 / 0,1,2,3,4,5,6,7,8
    l = idx
    r = idx + M - 1

    pal = M // 2

    is_pal = True

    for i in range(pal):
        if text[l+i] != text[r-i]:
            is_pal = False
    if is_pal:
        for i in range(l, r+1):
            print(text[i], end = '')
        print()








            

