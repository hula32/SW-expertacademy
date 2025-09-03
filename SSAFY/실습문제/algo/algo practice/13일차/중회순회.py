def inorder(i):
    lft = i * 2
    rgt = i * 2 + 1

    if lft <= N:
        inorder(lft)
    print(tree[i], end = '')
    if rgt <= N:
        inorder(rgt)


for t in range(1, 11):
    N = int(input())

    tree = [''] * (N+1)

    for n in range(N):
        num = list(input().split())
        
        tree[int(num[0])] = num[1]

    print(f'#{t}', end= ' ')
    inorder(1)
    print()
