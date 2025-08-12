T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    for m in range(M): # 0, 1
        i, j = map(int, input().split())
        i -= 1

        for idx in range(1, j+1): # 1, 2
            if i-idx < 0 or i+idx >= N:
                break

            if arr[i-idx] == arr[i+idx]:
                arr[i-idx] = (arr[i-idx]+1) % 2
                arr[i+idx] = (arr[i+idx]+1) % 2
    
    print(f'#{t}', *arr)





    

