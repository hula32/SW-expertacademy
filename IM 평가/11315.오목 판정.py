T = int(input())

for t in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]

    result = "No"

    # 행
    count = 0
    for r in range(N):
        for c in range(N):
            if arr[r][c] == 'o':
                count += 1
            if arr[r][c] == '.':
                    if count >= 5:
                        result = "YES"
                    else:
                        count = 0
        if count >= 5:
            result = "YES"
    # 열
    count = 0               
    for c in range(N):
        for r in range(N):
            if arr[r][c] == 'o':
                count += 1
            if arr[r][c] == '.':
                    if count >= 5:
                        result = "YES"
                    else:
                        count = 0
        if count >= 5:
            result = "YES"
    # 대각선 (0,4)(1,3)(2,2)(3,1)(4,1)
    count = 0
    for r in range(N):
        for c in range(N):
            if N-1-r == c:
                if arr[r][c] == "o":
                    count += 1
                if arr[r][c] == '.':
                    if count >= 5:
                        result = "YES"
                    else:
                        count = 0
        if count >= 5:
            result = "YES"

    # 대각선 (0,0)(1,1)(2,2)(3,3)(4,4)
    count = 0
    for r in range(N):
        for c in range(N):
            if r == c:
                if arr[r][c] == "o":
                    count += 1
                if arr[r][c] == '.':
                    if count >= 5:
                        result = "YES"
                    else:
                        count = 0
        if count >= 5:
            result = "YES"
               
    print(f"#{t} {result}")
            


 
                        

