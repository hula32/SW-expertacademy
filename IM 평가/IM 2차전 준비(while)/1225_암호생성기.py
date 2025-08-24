# 8자리 암호 생성
# 8자리 숫자 입력 받기
# 첫번째 숫자 -1 => 맨 뒤로 보내기
# 두번째 숫자 -2
# 세번째 숫자 -3
# 네번째 숫자 -4
# 다섯번째 숫자 -5 => 한 사이클
# 0보다 작아지는 경우 0으로 유지, 프로그램 종료

for t in range(1, 11):
    input()
    data = list(map(int, input().split()))

    i = 0

    while 0 not in data:
        for num in range(1, 6):
            if data[0] - num > 0:
                data.append(data.pop(0)-num)
            elif data[0] - num <= 0:
                data.pop(0)
                data.append(0)
                break
    print(f'#{t}', *data)
            



