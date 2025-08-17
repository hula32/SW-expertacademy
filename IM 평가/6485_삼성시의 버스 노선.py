T = int(input())

for t in range(1, T+1):
    # 노선 개수
    
    N = int(input()) # 2
    rute = [] # [(1, 3), (2, 5)]
    for n in range(N): # 0, 1
        A, B = map(int, input().split()) # 1이상 3이하 / 2이상 5이하 버스 노선
        rute.append((A, B))

    count = [0] * 5001 # 정거장 지나는 노선 카운트

    for start, end in rute: 
        for r in range(start, end+1):
            count[r] += 1

    # 정거장 개수 및 번호
    P = int(input()) # 5
    station = []
    for p in range(P): # 1,2,3,4,5 정거장 번호
        print(p)
        number = int(input()) # 1/2/3/4/5
        station.append(count[number])
    
    # print(f'#{t}', *station)
    
    

    # print(f'#{t}', *station)






            






