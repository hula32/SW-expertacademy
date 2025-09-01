T = int(input())

for t in range(1, T+1):
    word = input()

    N = len(word)
    stack = []
    cnt = 0

    for i in range(N):
        if word[i] == '(':
            stack.append(word[i])

        elif word[i] == ')':
            stack.pop()

            if word[i-1] == '(':
                cnt += len(stack)
            
            else:
                cnt += 1
            

    print(f'#{t} {cnt}')
