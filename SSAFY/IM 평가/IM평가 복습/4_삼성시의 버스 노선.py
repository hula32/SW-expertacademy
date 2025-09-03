T = int(input())

for t in range(1, T+1):
    N = int(input())
    #  버스노선
    bus_line = []
    for n in range(N): # 1,3 / 2,5
        A, B = map(int, input().split())
        bus_line.append((A, B))
    
    count = [0] * 5001

    for start, end in bus_line:
        for i in range(start, end +1):
            count[i] += 1
    
    # 버스 번호에 카운트 배열 넣기
    P = int(input())
    bus_number = []
    for p in range(P):
        C = int(input())
        bus_number.append(count[C])

    
    print(f'#{t}', *bus_number)

        

    
