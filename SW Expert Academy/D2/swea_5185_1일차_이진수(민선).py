# 테스트 케이스의 수 입력받기
T = int(input())
# 테스트 케이스만큼 입력받기
for t in range(1, T + 1):
    a, b = input().split()
    # 입력받은 16진수를 숫자로 변경하기
    num = int(b, 16)
    # 자릿수 * 4(한 자리당 4비트)
    len_num = int(a) * 4

    print(f'#{t} {num:0{len_num}b}')