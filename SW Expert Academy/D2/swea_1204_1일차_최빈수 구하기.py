# 테스트 케이스의 수
T = int(input())
# 테스트 케이스만큼 입력받기
for t in range(1, T+1):
    N = int(input())
    scores = list(map(int, input().split()))
    # 배열 0~100점까지 만들기
    arr = [0] * 101 
    # 점수에 해당되는 인덱스 카운트 1하기
    for score in scores:
        arr[score] += 1
    
    max_idx = -1 # 가장 많은 점수(인덱스)
    max_count = 0 # 가장 많은 점수 개수
    # 최빈수 구하기(최빈수가 여러 개일 경우 가장 큰 점수 출력)
    for idx, count in enumerate(arr):
        if max_count == count:
            if max_idx < idx:
                max_idx = idx
        elif max_count < count:
            max_count = count
            max_idx = idx

    print(f'#{t} {max_idx}')
        
