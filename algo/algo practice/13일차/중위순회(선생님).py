T = 10
# LVR
def inorder(root):
    left_child = root * 2
    right_child = root * 2 + 1
    if left_child <= N:
        inorder(left_child)
    print(node[root], end='')
    if right_child <= N:
        inorder(right_child)

for t in range(1, T+1):
    N = int(input())

    node = [""] * (N+1)

    for n in range(N):
        num = list(input().split())
        # print(num[0], num[1])
        node[int(num[0])] = num[1]

        # node.append(num[1])
        

        '''
        num[0] : 정점 번호
        num[1] : 정점 문자
        num[2] : 해당 정점 왼쪽 자식
        num[3] : 해당 정점 오른쪽 자식

        '''
        
    # print(node)
    print(f'#{t}', end = ' ')
    inorder(1)
    print()


