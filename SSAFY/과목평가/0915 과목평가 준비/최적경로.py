# # 조건 1 : 중복되지 않은 모든 경로 방문
# # 조건 2 : 회사 -> 고객들 -> 집에서 가장 짧은 경로
# # 조건 3 :|x1 - x2|+|y1 - y2|

# T = int(input())
# def recur(start_x, start_y, total, cnt):
#     global min_rute
#     if cnt == N:
#         total += abs(start_x-home[0]) + abs(start_y-home[1])
#         min_rute = min(min_rute, total)
#         return
    
#     if min_rute < total:
#         return
    
#     for i in range(N):
#         if not visited[i]:
#             visited[i] = True
#             x = start_x - client_x[i]
#             y = start_y - client_y[i]
#             recur(client_x[i], client_y[i], total + (abs(x)+abs(y)), cnt+1)
#             visited[i] = False

# for t in range(1, T+1):
#     N = int(input())
#     num = list(map(int, input().split()))

#     company = num[0:2]
#     home = num[2:4]
#     client_x, client_y = num[4::2], num[5::2]


#     visited = [False] * N
#     min_rute = float("inf")
#     recur(company[0], company[1], 0, 0)

#     print(f'#{t} {min_rute}')


# 조건 1 : 중복되지 않은 모든 경로 방문
# 조건 2 : 회사 -> 고객들 -> 집에서 가장 짧은 경로
# 조건 3 :|x1 - x2|+|y1 - y2|


T = int(input())

def recur(start_x, start_y, cnt, total):
    global min_val
    if cnt == N:
        total += (abs(start_x-home[0])+ abs(start_y-home[1]))
        min_val = min(min_val, total)
        return
    
    if min_val < total:
        return
    
    for i in range(N): # 0, 1, 2, 3, 4 
        if not visited[i]:
            visited[i] = True
            x_y = abs(start_x - client_x[i]) + abs(start_y - client_y[i])
            recur(client_x[i], client_y[i], cnt + 1, total + x_y)
            visited[i] = False
    

for t in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))

    company = numbers[0:2]
    home = numbers[2:4]
    client_x, client_y = numbers[4::2], numbers[5::2]

    visited = [False] * N
    min_val = float("inf")

    recur(company[0], company[1], 0, 0) 
    
    print(f'#{t} {min_val}')