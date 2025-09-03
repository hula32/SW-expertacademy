def is_monotonous(n):
    s = str(n)
    for i in range(len(s)-1):
        if int(s[i]) > int(s[i+1]):
             return False
    return True

T = int(input())

for t in range(1, T+1):
    N = int(input()) #4
    numbers = list(map(int, input().split())) # 2 4 7 10

    answer = -1

    # 모든 경우의 수 곱하기 
    for i in range(N-1): # 0,1,2
        for j in range(i+1, N): # 1,2,3
                num = numbers[i] * numbers[j]
    
                # 곱한 수 중에 단조 증가하는 수 찾기
                if is_monotonous(num):
                     if num > answer:
                          answer = num
            
    print(f'#{t} {answer}')


    
        