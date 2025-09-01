# [0, 1, 1, 2, 0]
# 1번은 바로 오른쪽
# 2번부터 N-1까지는 왼쪽에 있는 작성되어있는 번호 이동해서 복귀
# 방문했던 곳이면 오른쪽으로 전진
# N에 도착하면 끝

N = 5
P = [0] + [0, 1, 1, 2, 0]

visited = [False] * (N+1)

idx = 1
visited[idx] = True
cnt = 0

while idx < N:
    idx += 1
    cnt += 1

    if idx == N:
        break

    if not visited[idx]:
        visited[idx] = True
        idx = P[idx]
        cnt += 1

print(cnt)


