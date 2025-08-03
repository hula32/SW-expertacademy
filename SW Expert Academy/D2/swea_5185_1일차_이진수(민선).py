# 테스트 케이스의 수 입력받기
T = int(input())
# 테스트 케이스만큼 입력받기
for t in range(1, T + 1):
    a, b = input().split()
    # 입력받은 16진수를 숫자로 변경하기
    num = int(b, 16)
    # 2진수로 변경해서 출력하기
    len_num = int(a) * 4

    print(f'#{t} {num:0{len_num}b}')