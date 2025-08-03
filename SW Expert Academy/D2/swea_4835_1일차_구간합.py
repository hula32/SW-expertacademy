# 테스트 케이스 개수
T = int(input())
# 테스트 케이스 개수만큼 입력받기
for t in range(1, T+1):
    N, M = map(int,input().split())
    int_val = list(map(int,input().split()))

    min_val = 99999
    max_val = -99999
    
    # int_val 리스트 끝까지 돌아가면서 M개씩 더해서 비교하기
    for a in range(N-M+1) :
        # M개씩 더해서 최소값, 최대값 찾기
        num_sum = sum(int_val[a:a+M])
        if min_val > num_sum :
            min_val = num_sum
        if max_val < num_sum :
            max_val = num_sum
    # 최대값 - 최소값
    result = max_val - min_val

    print(f'#{t}', result)
        

