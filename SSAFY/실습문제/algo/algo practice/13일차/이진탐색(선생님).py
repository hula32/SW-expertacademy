T = int(input())


def inorder(i):
    global tree, cnt
    # i: 현재 부모 노드의 인덱스
    lft_child = i*2
    rgt_child = i*2 + 1

    # 1. L: 왼쪽 트리가 있다면 왼쪽 트리먼저 탐색
    if lft_child <= N: # N개의 노드만 고려
        inorder(lft_child)
    
    # 2. V: 현재 노드 방문
    tree[i] = cnt
    cnt += 1

    # 3. R: 오른쪽 트리가 있다면 오른쪽 트리 탐색
    if rgt_child <= N:
        inorder(rgt_child)




for tc in range(1, T+1):
    N = int(input())
    # 1부터 N까지의 숫자를 중위순회하면서 
    # 완전이진트리에 채우기

    tree = [0] * (N+1) # 완전이진트리
    cnt = 1 # 1부터 카운트를 하면서 숫자 채워나가기
    # 중위순회하면서 중위순회의 순서대로 채울 숫자

    inorder(1) # 루트 노드부터 탐색시작

    print(f"#{tc} {tree[1]} {tree[N//2]}")
    # 루트 노드와 N//2번 인덱스의 노드 출력