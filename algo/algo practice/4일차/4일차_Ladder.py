

for t in range(1, 11):
    input()
    
    arr = [list(map(int, input().split())) for _ in range(100)]
    
    arr_r, arr_c = -1, -1
    for r in range(100):
        for c in range(100):
            if arr[r][c] == 2:
                arr_r, arr_c = r, c
                
    r, c = arr_r, arr_c

    while r > 0:
        if c - 1 >= 0 and arr[r][c-1] == 1:
            while c - 1 >= 0 and arr[r][c-1] == 1:
                c -= 1
        elif c + 1 < 100 and arr[r][c+1] == 1:
            while c + 1 < 100 and arr[r][c+1] == 1:
                c += 1
        r -= 1

    print(f'#{t}, {c}')



       

    

              


       

