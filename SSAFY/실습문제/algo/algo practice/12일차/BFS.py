# def bfs(G, v):
#     visited = [0]*(n+1) # n : 정점의 개수이자 번호(1 ~ n번)
#     queue = []          # 큐 생성
#     queue.append(v)     # 시작점 v를 큐에 삽입
#     while queue:        # 큐가 비어있지 않은 경우
#         t = queue.pop(0) # 큐의 첫번째 원소 반환
#         if not visited[t]: # 방문되지 않은 곳이라면
#             visited[t] = True # 방문한 것으로 표시
#             visit(t)          # 정점 t에서 할 일
#             for i in G[t]:    # t와 연결된 모든 정점에 대해
#                 if not visited[i]: # 방문되지 않은 곳이라면
#                     queue.append(i) # 큐에 넣기

# # 인큐와 동시에 방문예정 표시

# def BFS(G, v, n): # 그래프 G, 탐색 시작점 v
#     visited = [0]*(n+1) # n : 정점의 개수
#     queue = []          # 큐 생성
#     queue.append(v)     # 시작점 v를 큐에 삽입
#     visited[v] = 1
#     while queue:            # 큐가 비어있지 않은 경우
#         t = queue.pop(0)    # 큐의 첫번째 원소 반환
#         visit(t)
#         for i in G[t]:      # t와 연결된 모든 정점에 대해
#             if not visited[i]:  # 인큐되지 않은 곳이라면
#                 queue.append(i) # 큐에 넣기
#                 visited[i] = visited[t] + 1 # n으로 부터 1만큼


'''
7 8 v : 정점 수(마지막 정점) - 1~7 또는 0~7 / E : 8개의 쌍
4 2 1 2 1 3 5 2 4 6 5 6 6 7 3 7

'''

def bfs(s, V): # 상황에 맞게 변형에서 사용
    # 초기화
    visited = [0] * (V + 1)    # visited 생성
    q = [s]    # 큐 생성
                # 시작점 인큐
    visited[s] = 1    # 시작점 인큐 표시
    # 반복
    while q: # 탐색할 정점이 남아 있으면
        t = q.pop(0) # 디큐
        print(t) # visit(), 방문 정점 출력
        for w in adj_lst[t]:        # 인접하고 미방문인 정점 인큐, 인큐 표시
            if visited[w] == 0:
                q.append(w)
                visited[w] = visited[t] + 1

    return

V, E = map(int, input().split()) # 마지막 정점, 간선 수
arr = list(map(int, input().split()))

# 그래프를 저장하는 방법 2가지
# 인접 리스트  / 인접 행렬
# - 인접리스트 : 
# - 간단한 인접 정보만 얻을 때 (2차원 리스트)
# - 행번호가 정점 번호

adj_lst = [[] for _ in range(V+1)] # V번행까지 준비
# 1번 방법
for i in range(E):
    v1, v2 = arr[i*2], arr[i*2*1]
# 2번 방법
# for i in range(0, E*2, 2):
#     v1, v2 = arr[i], arr[i+1]
    adj_lst[v1].append(v2)
    adj_lst[v2].append(v1) # 방향 표기가 없는 경우 양방향으로 저장 / 있는 경우 상황에 따라 둘 중 1개 사용

bfs(1, V)


