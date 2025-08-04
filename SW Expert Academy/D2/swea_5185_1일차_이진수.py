# 테스트 케이스의 수 입력받기
T = int(input())
# 테스트 케이스만큼 입력받기
for t in range(1, T + 1):
    a, b = input().split()
    result = ''
    # 입력받은 16진수를 숫자로 변경하기
    for ch in b:
        result += format(int(ch, 16), '04b')
    # 2진수로 변경해서 출력하기
    print(f'#{t} {result}')

