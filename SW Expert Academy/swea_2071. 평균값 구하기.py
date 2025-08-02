# 테스트 케이스 개수 입력받기
test = int(input())
# 평균값 리스트에 담기
average = []

# 테스트 케이스 개수만큼 입력받기
for t in range(test):
    test_case = map(int,input().split())

    total = 0
    count = 0
    # 합계와 입력받은 개수 나눠서 평균 구하기
    for case in test_case:
        total += case
        count += 1
    result = total / count
    # 평균값 리스트에 저장하기
    average.append(result)
# 테스트 케이스만킁 출력하기
for t in range(test):
    print(f'#{t+1}', round(average[t]))


