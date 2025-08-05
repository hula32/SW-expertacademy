T = int(input())

for t in range(1, T+1):
    words = input()
    stack = []

    for ch in words:
        if stack and stack[-1] == ch:
            print(stack)
            stack.pop()
            # print(stack)
        else:
            stack.append(ch)

    print(f'#{t} {len(stack)}')

# --------------------------
# 테스트 케이스의 개수를 입력받음
T = int(input())

# 각 테스트 케이스에 대해 반복
for t in range(1, T + 1):
    # 문자열 입력 받기
    words = input()
    
    # 문자를 저장할 스택 생성
    # 스택은 마지막에 들어온 값을 쉽게 꺼낼 수 있어서, 연속된 문자를 비교/제거할 때 유용함
    stack = []

    # 문자열의 각 문자를 하나씩 확인
    for ch in words:
        # 스택이 비어있지 않고, 스택의 가장 마지막 문자와 현재 문자가 같으면
        if stack and stack[-1] == ch:
            stack.pop()  # 연속된 같은 문자이므로 제거 (스택에서 꺼냄)
        else:
            stack.append(ch)  # 연속되지 않은 문자이므로 스택에 추가

    # 최종적으로 스택에 남아있는 문자의 개수가 연속된 문자를 제거하고 남은 문자열의 길이
    print(f'#{t} {len(stack)}')