# 테스트 케이스 개수
T = int(input())


# 테스트 케이스만큼 입력받기
for t in range(1, T+1):
    # 2차원 배열 만들기
    arr = [[0] * 10 for _ in range(10)]
    # 값 입력 받기
    N = int(input()) # 칠할 영역의 개수 N
    for n in range(1, N+1):
        r1, c1, r2, c2, color = list(map(int, input().split())) 
        # r1, c1 = 왼쪽 위 모서리 인덱스  
        # r2, c2 = 오른쪽 아래 모서리
        # color = 색상 정보 

        # 주어진 행과 열의 값을 행 우선 순회하면서 색깔 입력하기
        for r in range(r1, r2+1):
            for c in range(c1, c2+1):
                arr[r][c] += color
                
        ## 현재 입력된 2차원 배열 확인하기   
        # for r in range(10):
        #     for c in range(10):
        #         print(f"{arr[r][c]}  ", end = '')
        #     print()

    # 색깔이 겹친 곳 카운트 세기
    count = 0       
                    
    for r in range(10):
        for c in range(10):
            if arr[r][c] == 3:
                count += 1

    print(f'#{t} {count}')


               

            
                

