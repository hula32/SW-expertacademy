T = int(input())

for t in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]

    is_ok = True # 기본은 True 시작

    # 행 검사
    for r in range(9):
        check = [0] * 10 # 1~9까지 확인할 리스트
        for num in arr[r]:
            check[num] += 1
        if check[1:] != [1]*9: # 1~9가 각각 1번씩 나와야 함
            is_ok = False
            break

    # 열 검사
    if is_ok:
        for c in range(9):
            check = [0] * 10
            for r in range(9):
                check[arr[r][c]] += 1
            if check[1:] != [1]*9:
                is_ok = False
                break

    # 3 * 3 블록 검사
    # 큐브 확인 : 0, 3, 6 기준으로 칸을 나눠서 점검
    if is_ok:
        for p in range(0, 9, 3): # 0, 3, 6
            for q in range(0, 9, 3):
                check = [0] * 10
                for i in range(3):
                    for j in range(3):
                        num = arr[p+i][q+j]
                        check[num] += 1
                if check[1:] != [1]*9:
                    is_ok = False
                    break
        
    print(f'#{t} {1 if is_ok else 0}')

            
    