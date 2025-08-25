T = int(input())

for t in range(1, T+1):
    N = int(input())
    # input을 버리고 싶을 때, input()만 쓰면 됨

    # 1의 연속된 최대 길이
    answer = 0 # 초기값
    numbers = list(map(int, input()))
    # 안쪽부터 쓰는 습관 키우기

    one_count = 0
    for number in numbers:
        if number: # == 1을 없애도 됨 / True이기 때문
            one_count += 1
            # continue

        else:
            if one_count > answer:
                answer = one_count # answer = max(answer, one_count) 으로 구현 가능
            one_count = 0 # 초기화
        
        # answer = max(answer, one_count)
        # one_count = 0
        # 위에 continue를 사용할 경우, else로 자동으로 내려옴

        # if 조건:
        #     continue 
        # for문 안에서 if continue 문이 있으면 의미 없음

        # if 조건:
        #   break
        # 의미 있음
    
    answer = max(answer, one_count)

    print(f'#{t} {answer}')

T = int(input())

for t in range(1, T+1):
    N = int(input())
    # input을 버리고 싶을 때, input()만 쓰면 됨

    # 1의 연속된 최대 길이
    answer = 0 # 초기값
    numbers = input()
    # 안쪽부터 쓰는 습관 키우기

    one_count = 0
    for number in numbers:
        if number == '1': # == 1을 없애도 됨 / True이기 때문
            one_count += 1
            continue
        
        answer = max(answer, one_count)
        one_count = 0

    answer = max(answer, one_count)

    print(f'#{t} {answer}')

    


    