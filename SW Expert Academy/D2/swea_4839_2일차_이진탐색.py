# 이진탐색 함수 만들기
def get_binary_search_cnt(l, r, target_num):

    cnt = 0

    while l < r:
        c = (l + r) // 2
        cnt += 1
        # print(f"l={l}, r={r}, c={c}, cnt={cnt}")
        if c == target_num:
            break
        elif c < target_num:
            l = c
        else:
            r = c
    
    return cnt



T = int(input())


for t in range(1, T+1):
    P, A, B = list(map(int, input().split())) # 전체쪽수, A가 찾을 번호, B가 찾을 번호
    
    a_cnt = get_binary_search_cnt(1, P, A)
    b_cnt = get_binary_search_cnt(1, P, B)

    if a_cnt < b_cnt:
        print(f"#{t} A")
    elif b_cnt < a_cnt:
        print(f"#{t} B")
    else:
        print(f"#{t} 0")




