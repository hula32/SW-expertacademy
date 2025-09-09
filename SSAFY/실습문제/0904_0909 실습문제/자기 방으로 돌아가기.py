# prev_end보다 start 수가 더 작으면 cnt + 1

T = int(input())

for t in range(1, T+1):
    N = int(input())

    room_num = [0] * 201

    for _ in range(N):
        start, end = map(int, input().split())

        s = (start + 1) // 2
        e = (end + 1) // 2

        if s > e:
            s, e = e, s
        
        for i in range(s, e + 1):
            room_num[i] += 1
        
    
    print(f'#{t} {max(room_num)}')

