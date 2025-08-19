
icp = {'(':3, '*':2, '/':2, '+':1, '-':1}
isp = {'(':0, '*':2, '/':2, '+':1, '-':1}

for tc in range(1, 11):
    N = int(input())
    infix = input() # 입력, 중위 표기법
    postfix = '' # 후위표기식


    stack = []
    for x in infix:
    # for i in range(N):
    #     ifn infix[i] == ... 둘 다 작동하는게 정상
        if x in '*+': # 토큰이 연산자인 경우
        # 스택이 비어있거나, top(마지막 저장원소[-1])의 우선순위가 높으면
            while stack and isp[stack[-1]] >= icp[x]: # 스택 마지막 원소의 우선순위가 x와 높거나 같으면
                postfix += stack.pop()
            stack.append(x) # 스택이 비어있거나, top(마지막 저장원소[-1])의 우선순위가 높으면 push
        else: # 피연산자인 경우
            postfix += x
    while stack:
        postfix += stack.pop() # 남은 연산자 pop

    # postfix 연산
    for token in postfix:
        if token in '*+': # 연산자인 경우
            a = stack.pop() # 오른쪽 피연산자
            b = stack.pop() # 왼쪽 피연산자
            if token == '*':
                c = b * a
            elif token == '+':
                c = b + a
            stack.append(c) # 연산 결과 push
        else: # 피연산자인 경우
            stack.append(int(token))
    print(f'#{tc} {stack.pop()}')


