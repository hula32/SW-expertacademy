T = int(input())

def test(arr):
    stack = []

    for a in arr:
        if a == '{' or a == '(':
            stack.append(a)
        elif a == '}':
            if len(stack) > 0 and stack[-1] == '{':
                stack.pop()
            else:
                return 0
        elif a == ')':
            if len(stack) > 0 and stack[-1] == '(':
                stack.pop()
            else:
                return 0
    
    if len(stack) > 0 :
        return 0
    else:
        return 1

for t in range(1, T+1):
    arr = input().strip()

    ans = test(arr)

    print(f'#{t} {ans}')

