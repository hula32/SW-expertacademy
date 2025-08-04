# 테스트 케이스 개수
T = int(input())
# 테스트 개수만큼 입력받기
for t in range(1, T+1):
    N = int(input())
    # 소인수분해 숫자(나눌 숫자)
    number = [11, 7, 5, 3, 2]
    # 나머지 없이 나누어 떨어지는 횟수 저장
    n_list = ''
    # 소인수 분해
    for n in number:
        cnt = 0
        if N % n != 0:
            n_list += str(cnt)
            
        while N % n == 0:
            cnt += 1
            N = N / n
            if N % n != 0:
                n_list += str(cnt)
                if cnt == 0:
                    n_list += str(cnt)
            elif N == 1:
                break
    # 값 사이 공백 넣기
    n_list = " ".join(map(str, n_list))

    print(f'#{t} {n_list[::-1]}')