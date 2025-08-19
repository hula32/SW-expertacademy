T = int(input())

for t in range(1, T+1):
    N = int(input())

    # 버스 노선
    bus_line = []
    for n in range(N):
        A, B = map(int, input().split())
        bus_line.append((A, B))

    bus_number = [0] * 5001

    # 버스 번호
    for start, end in bus_line:
        for i in range(start, end+1):
            bus_number[i] += 1

    P = int(input())
    bus_count = []
    for p in range(P):
        C = int(input())
        bus_count.append(bus_number[C])
    
    