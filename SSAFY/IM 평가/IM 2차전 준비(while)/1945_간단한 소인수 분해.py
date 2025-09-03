T = int(input())

for t in range(1, T+1):
    N = int(input())


    num = [11, 7, 5, 3, 2]
    i = 0
    result = [0] * 5
    cnt = 0


    # 몫이 1이 될 때까지
    while N != 1:
    
        if N % num[i] == 0:
            cnt += 1
            N /= num[i]
        if N % num[i] != 0:
            result[i] = cnt
            cnt = 0
            i += 1

    
    print(f'#{t}' , *result[::-1])
    #1 3 2 2 3 1
#2 6 1 2 3 0
#3 6 4 2 0 1
#4 0 0 2 3 0
#5 0 3 4 0 1
#6 4 4 1 0 0
#7 7 3 0 3 0
#8 0 8 0 0 0
#9 0 0 2 0 0
#10 1 3 3 2 0



