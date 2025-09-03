for t in range(1, 11):
    input()
    N = input()

    out = ''

    stack = []

    for n in N:
        if n == '+':
            stack.append(n)
        else:
            out += n 
    
    while stack:
        out += stack.pop()

    
    stack2 = []

    for c in out:
        if '0' <= c <= '9':
            stack2.append(int(c))
        elif c == '+':
            num1 = stack2.pop()
            num2 = stack2.pop()
            stack2.append(num2+num1)
    
    print(f'#{t} {stack2.pop()}')
    
