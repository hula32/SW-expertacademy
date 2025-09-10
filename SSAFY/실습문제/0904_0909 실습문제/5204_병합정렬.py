T = int(input())

def merge(lft, rgt):
    arr = [0] * (len(lft) + len(rgt))
    l, r = 0, 0

    while l < len(lft) and r < len(rgt):
        if lft[l] < rgt[r]:
            arr[l + r] = lft[l]
            l += 1

        else:
            arr[l + r] = rgt[r]
            r += 1

    while l < len(lft):
        arr[l + r] = lft[l]
        l += 1

    while r < len(rgt):
        arr[l + r] = rgt[r]
        r += 1

    return arr

def merge_sort(li):
    if len(li) == 1:
        return li
    
    mid = len(li) // 2
    lft = li[:mid]
    rgt = li[mid:]

    lft_sort = merge_sort(lft)
    rgt_sort = merge_sort(rgt)

    return merge(lft_sort, rgt_sort)
    

for t in range(1, T+1):
    N = int(input())
    number = list(map(int, input().split()))

    sorted_arr = merge_sort(number)
    print(f'#{t}' , *sorted_arr)