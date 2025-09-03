T = int(input())

for t in range(1, T+1):
    line = input()

    N = len(line)
    total_cnt = 0
    cnt = 0

    for i in range(N):
        if line[i] == '(' :
            cnt += 1
        
        elif line[i] == ')':
            cnt -= 1
            if line[i -1] == '(':
                total_cnt += cnt
            else:
                total_cnt += 1

    print(f'#{t} {total_cnt}')
        