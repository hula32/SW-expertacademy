import datetime

# 테스트 개수 입력 받기
test = int(input())

# 년월일 입력받기
for t in range(1,test+1):
    date = int(input())
    year = date // 10000
    month_t = date % 10000
    month = month_t // 100
    day = date % 100
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12 :
        if day <= 31 and day > 0 :
            print(f"#{t} {year:04d}/{month:02d}/{day:02d}")
        else :
            print(f"#{t} -1")
    if month == 4  or month == 6 or month == 9 or month == 11 :
        if day <= 30 and day > 0 :
            print(f"#{t} {year:04d}/{month:02d}/{day:02d}")
        else :
            print(f"#{t} -1")
    if month == 2 :
        if day <= 28 and day > 0 :
            print(f"#{t} {year:04d}/{month:02d}/{day:02d}")
        else :
            print(f"#{t} -1")
    if month == 0 :
        print(f"#{t} -1")



