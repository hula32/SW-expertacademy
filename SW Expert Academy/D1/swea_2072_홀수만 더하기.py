# 테스트 케이스 개수 입력받기
test = int(input())
# 홀수 합계 리스트에 저장
result = []
# 테스트 케이스 개수만큼 입력받기
for t in range(test):
    test_case = map(int,input().split())
    total = 0
    # 홀수값만 더하고, 리스트에 저장
    for case in test_case:
        if case % 2 == 1:
            total += case
    result.append(total)
# 리스트에 저장된 값만큼 인덱스를 이용하여 결과값 도출
for t in range(test):
    print(f'#{t+1}',result[t])
    

# T = int(input())
# for t in range(1, T+1):
# print(f'#{t+1}',result[t])