# 테스트 케이스 개수
T = int(input())
# 테스트 케이스 개수만큼 입력받기
for t in range(1, T+1):
    N, M = map(int,input().split())
    int_val = list(map(int,input().split()))
    min_val = 99999
    max_val = -99999
    # result = []
    # 입력값 정렬
    for a in range(N-M+1) :
        num_sum = sum(int_val[a:a+M])
        if min_val > num_sum :
            min_val = num_sum
        if max_val < num_sum :
            max_val = num_sum
    
    # # 입력값 중 M개만큼 최소값끼리 더하기
    # min_val = sum(int_val[:M])
    # print(min_val)
    # # 입력값 중 M개만큼 최대값끼리 더하기
    # max_val = sum(int_val[-M:])
    # print(max_val)
    # # 최대값 - 최소값
    result = max_val - min_val
    #result.append(max_val - min_val)

    print(f'#{t}', result)
        

