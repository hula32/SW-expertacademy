T = int(input())

for t in range(1, T+1):
    N = int(input())

    line = []
    for n in range(N):
        A, B = map(int, input().split())
        line.append((A, B))

    visited = [0] * 5001

    for start, end in line:
        for i in range(start, end+1):
            visited[i] += 1

    bus_cnt = []
    P = int(input())
    for p in range(P):
        bus_number = int(input())
        bus_cnt.append(visited[bus_number])


    print(f'#{t}', *bus_cnt)
