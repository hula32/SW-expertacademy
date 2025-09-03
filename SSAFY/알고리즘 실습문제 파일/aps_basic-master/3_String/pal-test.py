# text = "abcdefcba"

# l = 0
# r = len(text) - 1

# num_pairs = len(text) // 2

# is_pal = True # 일단 회문이라고 가정
# for step in range(num_pairs):
#     print(l + step, r - step, '비교')
#     if text[l + step] != text[r - step]: # 대칭된 문자가 서로 다르다면
#         is_pal = False

# print(is_pal)




# text = "abcdedfba"

# l = 0
# r = len(text) -1 # 8~

# pal = len(text) // 2

# is_pal = True
# for idx in range(pal):
#     if text[l+idx] != text[r-idx]:
#         is_pal = False

# print(is_pal)



text = "abcdedcba"

l = 0
r = len(text)-1

step = len(text) // 2

is_pal = True

for idx in range(step):
    if text[l+idx] != text[r-idx]:
        is_pal = False

print(is_pal)






