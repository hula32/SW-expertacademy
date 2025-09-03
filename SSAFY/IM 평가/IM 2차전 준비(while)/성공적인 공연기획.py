T = int(input())

for t in range(1, T+1):
    num = list(map(int, input())) # 110011

    cnt = 0
    hire = 0
    for i in range(len(num)): # 0,1,2,3,4,5
        if cnt >= i:
            cnt += num[i]
        elif cnt < i:
            hire += i - cnt
            cnt += i - cnt + num[i]
            

    print(f'#{t} {hire}')


