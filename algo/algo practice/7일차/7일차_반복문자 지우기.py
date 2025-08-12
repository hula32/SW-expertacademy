T = int(input())

for t in range(1, T+1):
    word = input()
    stack = []

    for ch in word: # N N N A S B B S N V
        if stack and stack[-1] == ch:
            stack.pop()
        else:
            stack.append(ch)
    

    print(f'#{t}', len(stack) )
            
