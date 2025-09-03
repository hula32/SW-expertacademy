import sys
input = sys.stdin.readline

T = int(input())

for t in range(T):
    PS = input().strip()
    stack = []
    valid = True # 올바른 괄호 문자열인지 체크하는 플래그

    for ps in PS:
        if ps == '(':
            stack.append(ps)
        else:
            if stack:
                stack.pop()
            else:
                valid = False
                break
       
    if stack:
        valid = False

    if valid:
        print("YES")
    else:
        print("NO")

    