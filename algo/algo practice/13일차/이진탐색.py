def inorder(i):
    global tree
    global cnt

    lft_child = i * 2
    rgt_child = i * 2 + 1

    if lft_child <= N:
        inorder(lft_child)

    cnt += 1
    tree[i] = cnt
    
    if rgt_child <= N:
        inorder(rgt_child)



T = int(input())

for t in range(1, T+1):
    N = int(input())

    tree = [0] * (N+1)
    cnt = 0    
    inorder(1)

    # print(tree)

    print(f'#{t} {tree[1]} {tree[N//2]}')