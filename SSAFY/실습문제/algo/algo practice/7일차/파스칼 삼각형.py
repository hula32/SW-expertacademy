T = int(input())

for t in range(1, T+1):
    N = int(input()) # 4

    stack = [[] for _ in range(N)]
    stack[0].append(1)
    stack[1].append(1)
    stack[1].append(1)

    for i in range(2, N): # 2,3
        stack[i].append(1)
        for j in range(i-1):
            stack[i].append(stack[i-1][i-1]+stack[i-1][i+1])
        stack[i].append(1)
    
    print(stack)

        

