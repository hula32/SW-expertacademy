T = int(input())

for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    dr = [0, 0, -1, 1]
    dc = [1, -1, 0, 0]

    def is_min(r, c):
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if 0 <= nr < N and 0 <= nc < N:
                if arr[r][c] < arr[nr][nc]:
                    return False # 바로 종료
        return True

    def find_min(r, c):

        min_val = arr[r][c]

        min_r, min_c = -1, -1

        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if 0 <= nr < N and 0 <= nc < N:
                if arr[nr][nc] < min_val:
                    min_val = arr[nr][nc]
                    min_r, min_c = nr, nc
        
        return min_r, min_c

        
    def simulation(r, c):
        cnt = 1

        while not is_min(r, c): # is_min : 작은 값이 있는 없는 경우 멈추고, 있으면 이동
            nr, nc = find_min(r, c)
            r, c = nr, nc
            cnt += 1

        return cnt



    max_cnt = 0
    for r in range(N):
        for c in range(N):
            cnt = simulation(r, c) # simulation 함수: (r,c) 출발점으로 공굴리기를 진행한 후 칸의 수를 반환하는 함수

            if cnt > max_cnt:
                max_cnt = cnt

    print(max_cnt)
            



                

                

                

            
            
                        



    
           