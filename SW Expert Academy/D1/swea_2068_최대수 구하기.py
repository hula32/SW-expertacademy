# 테스트 개수 입력받기
test = int(input())

# 최대 결과값 저장 리스트
result = []

# 테스트 개수만큼 입력받기
for t in range(test):
    test_case = map(int, input().split())
    # 최대값 초기 값 설정
    max_val = 0
    # 최대값 비교
    for case in test_case:
        if case > max_val:
            max_val = case
    # 최대값 저장
    result.append(max_val)
# 결과 호출
for t in range(test):
    print(f'#{t+1}', result[t])


