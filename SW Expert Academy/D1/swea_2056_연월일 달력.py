# 테스트 케이스 개수
T = int(input())
# 테스트 개수만큼 입력받기
for t in range(1, T+1):
    t_case = int(input())

    # 년/월/일 분리
    year = t_case // 10000
    month_t = t_case % 10000
    month = month_t // 100
    day = t_case % 100

    # 1일부터 각각의 달에 해당하는 날짜까지의 값
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        if day <= 31 and day >= 0:
            print(f'#{t} {year:04d}/{month:02d}/{day:02d}')
        else:
            print(f'#{t} -1')
    if month == 4 or month == 6 or month == 9 or month == 11:
        if day <= 30 and day >= 0:
            print(f'#{t} {year:04d}/{month:02d}/{day:02d}')
        else:
            print(f'#{t} -1')
    if month == 2:
        if day <= 28 and day >= 0:
            print(f'#{t} {year:04d}/{month:02d}/{day:02d}')
        else:
            print(f'#{t} -1')
    if month == 0:
        print(f'#{t} -1')