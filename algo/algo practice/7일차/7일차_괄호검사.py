T = int(input())

"""
함수는
return 문을 만나면 바로 종료한 후, 호출한 곳으로 되돌아감.

=> 괄호검사를 하다가 틀린부분을 발견하면, 그 이후는 볼것도 없이 0을 반환

"""

def check_text(text):
    stack = []
    for c in text:
        if c == '(' or c == '{':
            stack.append(c)
        elif c == ')':
            if len(stack) > 0 and stack[-1] == '(':
                stack.pop()
            else:
                return 0 # 하는 이유? 짝이 안맞으므로 바로 0을 리턴
        elif c == '}':
            if len(stack) > 0 and stack[-1] == '{':
                stack.pop()
            else:
                return 0 # 짝이 안맞으므로 리턴
            
    if len(stack) > 0:
        return 0 # 모든 것을 다 검사했는데, 스택에 괄호가 남아있다 => 괄호의 짝이 안맞음 => 0
    else: # 스택이 비어있다면 => 모든 것이 짝이 맞음
        return 1 # 1


for t in range(1, T+1):
    str = input().strip() #하는 이유 : " print('{} {}'.format(1, 2))   " , input 문자열 앞뒤에 공백이 있다면 제거하기 위해

    ans = check_text(str)

    print(f'#{t} {ans}')
