T = int(input())

for t in range(1, T+1):
    N, K, E = map(int, input().split())

    number = []
    for e in range(E):
        start, end = map(int, input().split())
        number.append((start, end))

    arr = [0] * (N+1)
    # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

    for n in range(1, N+1): # 게임판 만들기
        arr[n] = n


    def dfs(i):

        num = [0] * K
        visited = [False] * 7

        while i < K:
            for j in range(1, 7): # 1,2,3,4,5,6
                if not visited[j]:
                    visited[j] = True
                    num[i] = j
                    i += 1
                    dfs(i)
                    visited[j] = False
        return num

    dfs(1)










