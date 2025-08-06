T = int(input())

for t in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]

    # 행의 개수
    rows = len(arr)

    # 열의 개수
    cols = len(arr[0])

    # 부분배열의 크기
    k = 3
    l = 3

    for r in range(rows):
        for c in range(cols):
            # 큐브 확인 : 0, 3, 6 기준으로 칸을 나눠서 점검
            if arr[r]

            # 열 확인
            # 같은 숫자 같은 인덱스에 카운트 세기
            cnt_c = [0] * 10

            for num in arr[r]:
                cnt_c[num] += 1
            
            # 행 확안
            cnt_r = [0] * 10

            for r in range(9):
                cnt_r[arr[r][c]] += 1

            # 카운트에 1이 아닌 숫자가 있으면 False
            is_ok = True
            for c in range(1, 10):
                if cnt_c[c] != 1:
                    is_ok = False
                    break
                if cnt_r[c] != 1:
                    is_ok = False
                    break
            
            if is_ok:
                print(1)
            else:
                print(0)
            
            


    #         # 3x3 격자
    #         sum_arr = [arr[x][c:c+l]for x in range(r, r+k)]

    #         and

    #         # 같은 줄 확인하기
    #         arr[r][c]
    #         if 같은 숫자가 겹치면: 0 출력
    #         아니면 : 1 출력

            


    
    # for r in range(rows):
    #     for c in range(cols):
    #         print(f'{r}, {c} {arr[r][c]}' , end=' ')
    #     print()
            