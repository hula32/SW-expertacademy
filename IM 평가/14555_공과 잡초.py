T = int(input())

for t in range(1, T+1):
    arr = input()

    cnt = 0

    for i in range(len(arr)-1):
        if arr[i] == '(':
            if arr[i+1] == ')' or '|':
                cnt += 1
        elif arr[i] == '|':
            if arr[i+1] == ')':
                cnt += 1
            

    print(f'#{t} {cnt}')


# while문

T = int(input())

for t in range(1, T+1):
    arr = input()
    N = len(arr)

    cnt = 0

    # while은 직접 인덱스를 지정
    i = 0

    # i : N-1까지 검사하길 바람
    # i : N이 되면 검사 불가능
    while i < N-1: # True
        if arr[i] == '(':
            if arr[i+1] == ')' or '|':
                cnt += 1
                i += 2 # 다음까지 검사하기 때문에 + 2 가능
                continue
        elif arr[i] == '|':
            if arr[i+1] == ')':
                cnt += 1
                i += 2
                continue

        i += 1
    

    print(f'#{t} {cnt}')

    
    # i == N 종료 False
