# 입력받기
num = int(input())

if num % 2 != 0:
    print(num * (num + 1) // 2)
elif num % 2 == 0:
    print((num//2) * (num+1))

