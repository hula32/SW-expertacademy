# 핵심
# 1. 조합 또는 부분집합 생성
# 2. 부분집합 방법
# - intertools.combinations 사용 -> 간단
# - 비트마스킹 -> 모든 부분집합 탐색
# - 재귀 백트래킹 -> N개를 뽑는 경우만 탐색

arr = list(range(1, 13))

T = int(input())

for t in range(1, T+1):
    N, K = list(map(int, input().split()))
    count = 0
    # N: 부분집합의 원소 개수
    # K: 원소의 합
    for bit in range(1<<len(arr)): # 0 ~ 2^12-1
        subset = []
        for i in range(len(arr)):
            if bit & (1<<i):
                subset.append(arr[i])
        # 부분집합 완성 후 조건 확인
        if len(subset) == N and sum(subset) == K:
            count += 1
    print(f'#{t} {count}')



