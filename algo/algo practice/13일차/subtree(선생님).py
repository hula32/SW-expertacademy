T = int(input())

def f(root):
    global node_cnt
    # 노드 카운트를 하나 늘리기
    node_cnt += 1
    # 왼쪽 자식이 있다면 왼쪽 자식을 루트 노드로 해서 탐색
    if lft_child[root] != 0:
        f(lft_child[root])
    # 오른쪽 자식이 있다면 오른쪽 자식을 루트 노드로 해서 탐색
    if rgt_child[root] != 0:
        f(rgt_child[root])

for tc in range(1, T+1):
    E, N = map(int, input().split())
    # E: 간선의 개수 => 노드의 개수는 E+1개
    # N: 탐색을 시작할 노드의 번호
    # 노드 번호는 1번부터 E+1번까지 존재

    lft_child = [0] * (E+2)
    rgt_child = [0] * (E+2)

    # child = [[0]*(E+2) for _ in range(2)]

    arr = list(map(int, input().split()))
    #  0    1   2   3 ...
    # 부모 자식 부모 자식 ..
    for i in range(E):
        parent = arr[i*2] # 2,2,1,5,6
        child = arr[i*2+1] # 1,5,6,3,4

        if lft_child[parent] == 0:
            lft_child[parent] = child
        else:
            rgt_child[parent] = child
    
    node_cnt = 0 # 노드의 개수
    f(N) # 주어진 번호를 root 노드로 하여 탐색 시작!

    print(f"#{tc} {node_cnt}")