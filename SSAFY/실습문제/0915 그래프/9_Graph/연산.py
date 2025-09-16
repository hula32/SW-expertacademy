from collections import deque

T = int(input())

# def bfs(node):
#     global result

#     if node == 7:
#         result += 1
#         return

#     q = deque([node])

#     while q:
#         v = q.popleft()

#         for i in range(4):
#             if i == 0:
#                 q.append(v+1)
#             elif i == 1:
#                 q.append(v - 1)
#             elif i == 2:
#                 q.append(v * 2)
#             elif i == 3:
#                 q.append(v - 10)




for t in range(1, T+1):
    N, M = map(int, input().split())

    result = 0
    visited = [0] * 
    bfs(N)

    print(f'#{t} {result}')
