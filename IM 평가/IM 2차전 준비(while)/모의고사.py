# T = int(input())

# for t in range(1, T+1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]

N = 3
arr = [[1, 2, 3], 
       [4, 5, 6], 
       [7, 8, 9]]

dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]
# 제일 길게 공 굴린 값


# 기준점
for r in range(N):
    result = 0
    for c in range(N):
        start_r, start_c = r, c

        cnt = 0
      
        while True:
            min_v = sorted([])
            cnt = 0
            for d in range(4):
                nr, nc = start_r + dr[d], start_c + dc[d]
                if 0 <= nr < N and 0 <= nc < N and arr[start_r][start_c] > arr[nr][nc] :
                    min_v.append((arr[nr][nc], nr, nc))
            if min_v:
                min_result = min_v[0][0]
                start_r, start_c = min_v[0][1], min_v[0][2]
                cnt += 1
            if result < cnt:
                result = cnt
            break

print(result)
            

            



                

                

                

            
            
                        



    
           