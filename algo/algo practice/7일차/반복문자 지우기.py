T = int(input())

for t in range(1, T+1):
    N = input().strip() #ABCCB
    stack = [] * len(N)

    for n in N:
        if stack and stack[-1] == n:
            stack.pop()
        else:
            stack.append(n)
    print(f'#{t} {len(stack)}')

