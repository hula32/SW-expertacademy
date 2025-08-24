T = int(input()) 

def f(i):
    global cnt
    cnt += 1

    if lft_child[i] != 0:
        f(lft_child[i])
    if rgt_child[i] != 0:
        f(rgt_child[i])


for t in range(1, T+1):
    E, N = map(int, input().split())

    lft_child = [0] * (E+2)
    rgt_child = [0] * (E+2)

    num = list(map(int, input().split())) # 2 1 2 3 1 6 5 3 6 4

    for i in range(E): # 0,1,2,3,4
        parent = num[i * 2]
        child = num[i * 2 + 1]

        if lft_child[parent] == 0:
            lft_child[parent] = child
        else:
            rgt_child[parent] = child
    
    cnt = 0
    f(N)

    print(f'#{t} {cnt}')