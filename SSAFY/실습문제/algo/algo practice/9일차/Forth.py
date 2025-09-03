T = int(input())

for t in range(1, T+1):
    N = input().split()

    stack = []
    result = 0

    for n in N:
        if n == '+':
            if len(stack) < 2:
                result = -1
                break
            n1 = int(stack.pop())
            n2 = int(stack.pop())
            stack.append(n2+n1)
        elif n == '-':
            if len(stack) < 2:
                result = -1
                break
            n1 = int(stack.pop())
            n2 = int(stack.pop())
            stack.append(n2-n1)
        elif n == '*':
            if len(stack) < 2:
                result = -1
                break
            n1 = int(stack.pop())
            n2 = int(stack.pop())
            stack.append(n2*n1)
        elif n == '/':
            if len(stack) < 2 or stack[-1] == 0:
                result = -1
                break
            n1 = int(stack.pop())
            n2 = int(stack.pop())
            stack.append(n2//n1)
        elif n == '.':
            if len(stack) != 1:
                result = -1
            else:
                result = stack.pop()
            break
        else:
            stack.append(int(n))
    
    if result == -1:
        print(f'#{t} error')
    else:
        print(f'#{t} {result}')


