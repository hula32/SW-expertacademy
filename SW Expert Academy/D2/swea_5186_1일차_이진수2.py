# 테스트 케이스 개수 입력 받기
T = int(input())
# 테스트 케이스만큼 값 입력 받기
for t in range(1, T + 1):
    num = float(input()) # 실수 입력받기
    number = num - int(num) # 소수점 이하만 출력

    result = ''
    count = 0

    while number != 0: # 0이 아닐 경우
        number *= 2 # 2를 곱해 정수 부분 추출
        bit = int(number) # 정수 부분(0 또는 1) 추출
        result += str(bit) 
        number -= bit # 정수를 제외한 부분만 다음 루프에 넘김
        count += 1
        # 소수점 자리가 13자리가 넘으면 호출
        if count > 13:
            result = 'overflow'
            break

    print(f'#{t} {result}')

    