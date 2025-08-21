# 최소 거리(간선)
# V : 종료 숫자
# E : 간선 수
# line : 간선 양쪽 노드 번호
# 출발노드 : S, 도착노드 G

# 4 2 1 2 1 3 5 2 4 6 5 6 6 7 3 7


# 0: []
# 1: [2, 3]
# 2: [4, 1, 5]
# 3: [1, 7]
# 4: [2, 6]
# 5: [2, 6]
# 6: [4, 5, 7]
# 7: [3, 6]

from collections import deque

def line(node, S, V, G):
    visited = [0] * (V+1)
    q = deque()
    q.append(S)
    visited[S] = 1

    while q:
        t = q.popleft()
        
        for i in node[t]:
            if not visited[i]:
                q.append(i)
                visited[i] = visited[t] + 1
    if visited[G]:
        return visited[G] -1
    else:
        return 0

T = int(input())

for t in range(1, T+1):
    V, E = map(int, input().split()) # 6, 5

    node = [[] for _ in range(V+1)]
    '''
    [[], [4, 3], [3, 5], [1, 2], [1, 6], [2], [4]]

    '''

    for e in range(E):
        A, B = map(int, input().split())
        v1, v2 = A, B
        node[A].append(v2)
        node[B].append(v1)
    
    S, G = map(int, input().split()) # 1, 6

    print(f'#{t} {line(node, S, V, G)}') # 함수 실행









    
    






        

