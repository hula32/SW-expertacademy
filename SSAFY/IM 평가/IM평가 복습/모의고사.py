T = int(input())

for t in range(1, T+1):
    N, K = map(int, input().split())

    # arr = [[0] * N] * 4
    arr = [[0] * N for _ in range(4)]

    count = 0

    for r in range(4): # 0,1,2,3
        for c in range(N): # 0,1,2,3,4
            
            for k in range(1, K+1): # 1, 2, 3
                if (r+c+1) % k == 0:   
                    if arr[r][c] == 0:
                        arr[r][c] += 1
                    else:                         
                        arr[r][c] -= 1

    for r in range(4): # 0,1,2,3
        for c in range(N): # 0,1,2,3,4
            if arr[r][c] == 1:
                count += 1
        # count += sum(arr[r])

            
        
    print(count)

# 4행 = j
# N열 = i

# (2, 3) -> (2+3+1) = 6 (k(3) 배수) 변함
# (i, j) 합 홀수면 k = 짝수 / 합 짝수면 k = 홀수

    

# 


    
       
# arr = [[0, 0, 0, 0, 0], 
#        [0, 0, 0, 0, 0], 
#        [0, 0, 0, 0, 0], 
#        [0, 0, 0, 0, 0]]

# N = 5
# K = 3