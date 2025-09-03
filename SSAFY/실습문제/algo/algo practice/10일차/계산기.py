
icp = {'(':3, '*':2, '/':2, '+':1, '-':1} # 밖에 있을 때의 우선 순위(클수록 높음)
isp = {'(':0, '*':2, '/':2, '+':1, '-':1} # 스택안에의 우선 순위(클수록 높음)

for t in range(1, 11):
    TC = int(input())
    exp = input()

# exp = ('9+5*2+1+3*')
    out = ''

    stack = []

    for c in exp:
        if c == '*':
            if not stack:
                stack.append(c)
            elif stack[-1] == '+':
                stack.append(c)
            else:
                while stack and stack[-1] == '*':
                    out += stack.pop()
                stack.append(c)

        elif c == '+':
            while stack:
                out += stack.pop()
            stack.append(c)

        else:
            out += c

    while stack:
        out += stack.pop()

    # 계산하기
    stack2 = [] # 숫자 스택

    for c in out:
        if '0' <= c <='9':
            stack2.append(int(c))
        elif c == '+':
            num1 = stack2.pop()
            num2 = stack2.pop()
            stack2.append(num1+num2)
        elif c == '*':
            num1 = stack2.pop()
            num2 = stack2.pop()
            stack2.append(num1*num2)

    print(f'#{t} {stack2.pop()}')






