def inorder(i):
    lft_child = i * 2
    rgt_child = i * 2 + 1

    if lft_child <= N:
        inorder(lft_child)
    print(tree[i], end = '')
    if rgt_child <= N:
        inorder(rgt_child)


for t in range(1, 11):
    N = int(input())

    tree = [''] * (N+1)

    for n in range(N):
        num = list(input().split())
        '''
        num[0] : 정점 번호
        num[1] : 정점 문자
 
        '''
        tree[int(num[0])] = num[1]


    print(f'#{t}', end = ' ')
    inorder(1)
    print()

      