# '''
# ( )( )((( )))
# ((( )((((( )( )((( )( ))((( ))))))
# ())
# (()
# )(
# '''
txt = input()

top = -1
stack = [0] * 100

ans = 1
for x in txt:
    if x == '(':    # 여는 괄호 push
        top += 1
        stack[top] = x
    elif x == ')':  # 닫는 괄호인 경우
        if top == -1:   # 스택이 비어있으면 (여는 괄호가 없으면 )
            ans = 0
            break   # for x
        else:           # 여는 괄호 하나 버림
            top -= 1    # pop
if top != -1:   # 여는 괄호가 남아있으면
    ans = 0

print(ans)

txt = input()

top = -1
stack = [0] * 100

ans = 1
for x in txt:
    if x == '(':
        top += 1
        stack[top] = x
    elif x == ')':
        if top == -1:
            ans = 0
            break
            
        else:
            top = -1
if top != -1:
    ans = 0

'''
( )( )((( )))
((( )((((( )( )((( )( ))((( ))))))
())
(())
)(
'''

T = input().strip()

stack = []

for t in T:
    if t == '(':
        stack.append(t)
    elif t == ')':
        if stack and stack[-1] == '(':
            stack.pop()
        else:
            print(-1)
            break

else:
    if stack :
        print(-1)
    else:
        print(1)
