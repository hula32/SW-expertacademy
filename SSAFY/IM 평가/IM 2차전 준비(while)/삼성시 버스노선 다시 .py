T = int(input())

for t in range(1, T+1):
    N = int(input())
    
    line = []
    for n in range(1, N+1):
        A, B = map(int, input().split())
        line.append((A, B))
    
    bus_station = [0] * 5001

    for start, end in line:
        for i in range(start, end +1):
            bus_station[i] += 1

    bus_cnt = []
    P = int(input())
    for p in range(1, P+1):
        j = int(input())
        bus_cnt.append(bus_station[j])

    print(f'#{t}', *bus_cnt)



    