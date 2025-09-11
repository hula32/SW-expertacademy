import heapq

T = int(input())

for t in range(1, T+1):
    N = int(input())

    heap = []
    result = []

    for n in range(N):
        cmd = list(map(int, input().split()))

        if cmd[0] == 1:
            heapq.heappush(heap, -cmd[1])

        elif cmd[0] == 2:
            if heap:
                max_val = -heapq.heappop(heap)
                result.append(max_val)
            else:
                result.append(-1)

    print(f'#{t}', *result)
