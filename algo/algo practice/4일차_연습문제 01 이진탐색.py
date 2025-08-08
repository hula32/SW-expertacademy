

def Search(l, r, key):

    cnt = 0

    while l < r:
        middle = (l+r)//2
        cnt += 1
        if middle == key:
            break
        elif middle > key:
            r = middle
        else:
            l = middle

    return cnt


T = int(input())

for t in range(1, T+1):
    P, A, B = map(int, input().split())

    a_search = Search(1, P, A)
    b_search = Search(1, P, B)

    if a_search < b_search:
        print(f'#{t} A')
    elif a_search > b_search:
        print(f'#{t} B')
    else:
        print(f'#{t} 0')
