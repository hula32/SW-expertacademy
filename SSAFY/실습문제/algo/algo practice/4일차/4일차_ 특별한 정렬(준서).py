T = int(input())
 
for test_case in range(1, T + 1):
    N = int(input())
    numbers = list(map(int, input().split()))
 
    numbers.sort() # 정렬
    result = []
 
    for i in range(N // 2 + 1):  # 짝수/홀수 대비
        if len(result) >= 10: # 출력개수를 10개로 제한
            break
        result.append(numbers[-(i + 1)])  # 큰 수
        if len(result) >= 10:
            break
        result.append(numbers[i])        # 작은 수
 
    print(f'#{test_case}', *result[:10])