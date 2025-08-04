# 테스트 케이스 개수
T = int(input())
# 테스트 개수만큼 입력받기
for t in range(1, T+1):
    str1 = list(input()) # ['X', 'Y', 'P', 'V']
    str2 = list(input()) # ['E', 'O', 'G', 'G', 'X', 'Y', 'P', 'V', 'S', 'Y']
    # 가장 많은 글자의 개수 저장
    str_cnt = [] # [1, 2, 1, 1]

    for s1 in str1:
        cnt = str2.count(s1)
        str_cnt.append(cnt)

    print(f'#{t} {max(str_cnt)}')