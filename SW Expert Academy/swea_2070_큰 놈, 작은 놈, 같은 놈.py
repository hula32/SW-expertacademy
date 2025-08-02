# 테스트 개수 입력받기
test = int(input())
# 결과값 리스트로 저장하기
result = []

# 테스트 개수만큼 입력받기
for t in range(test):
    test_case = map(int, input().split())
    # 결과값 저장
    r = []
    # 입력받은 값 비교하기
    for case in test_case:
        if not r:
            r.append(case)
        elif r[0] < case:
            r = "<"
        elif r[0] > case:
            r = ">"
        elif r[0] == case:
            r = "="
    # 저장된 저장값 결과값 리스트에 저장하기
    result.append(r)
# 결과값 테스트 개수만큼 출력하기
for t in range(test):
    print(f'#{t+1}', result[t])



